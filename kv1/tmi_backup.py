import codecs
import sys
import os
import zipfile
import psycopg2
import helper
import time

from tmi_conarea import tmi_conarea
from tmi_confinrel import tmi_confinrel
from tmi_dest import tmi_dest
from tmi_excopday import tmi_excopday
from tmi_financer import tmi_financer
from tmi_icon import tmi_icon
from tmi_jopa import tmi_jopa
from tmi_jopatili import tmi_jopatili
from tmi_line import tmi_line
from tmi_link import tmi_link
from tmi_notice import tmi_notice
from tmi_ntcassgnm import tmi_ntcassgnm
from tmi_operday import tmi_operday
from tmi_orunorun import tmi_orunorun
from tmi_orun import tmi_orun
from tmi_pegr import tmi_pegr
from tmi_pegrval import tmi_pegrval
from tmi_point import tmi_point
from tmi_pool import tmi_pool
from tmi_pujopass import tmi_pujopass
from tmi_pujo import tmi_pujo
from tmi_schedvers import tmi_schedvers
from tmi_specday import tmi_specday
from tmi_tili import tmi_tili
from tmi_timdemgrp import tmi_timdemgrp
from tmi_timdemrnt import tmi_timdemrnt
from tmi_tive import tmi_tive
from tmi_usrstar import tmi_usrstar
from tmi_usrstop import tmi_usrstop
from secret import username, password, sql_username, sql_password, sql_hostname, sql_port, sql_database

class tmi:
    def __init__(self, filename=None):
        self._filename = filename
        self._processors = {
            'CONAREA': tmi_conarea(),
            'CONFINREL': tmi_confinrel(),
            'DEST': tmi_dest(),
            'EXCOPDAY': tmi_excopday(),
            'FINANCER': tmi_financer(),
            'ICON': tmi_icon(),
            'JOPA': tmi_jopa(),
            'JOPATILI': tmi_jopatili(),
            'LINE': tmi_line(),
            'LINK': tmi_link(),
            'NOTICE': tmi_notice(),
            'NTCASSGNM': tmi_ntcassgnm(),
            'OPERDAY': tmi_operday(),
            'ORUNORUN': tmi_orunorun(),
            'ORUN': tmi_orun(),
            'PEGR': tmi_pegr(),
            'PEGRVAL': tmi_pegrval(),
            'POINT': tmi_point(),
            'POOL': tmi_pool(),
            'PUJOPASS': tmi_pujopass(),
            'PUJO': tmi_pujo(),
            'SCHEDVERS': tmi_schedvers(),
            'SPECDAY': tmi_specday(),
            'TILI': tmi_tili(),
            'TIMDEMGRP': tmi_timdemgrp(),
            'TIMDEMRNT': tmi_timdemrnt(),
            'TIVE': tmi_tive(),
            'USRSTAR': tmi_usrstar(),
            'USRSTOP': tmi_usrstop(),
        }
        self.types = [
            {'name': 'Recordtype', 'aard': 'x', 'type': 'A', 'length': 10 },
            {'name': 'Version', 'aard': 'x', 'type': 'N', 'length': 2 },
            {'name': 'Implicit', 'aard': 'x', 'type': 'B', 'length': 1 },
            {'name': 'DataOwnerCode', 'aard': '#', 'type': 'A', 'length': 10 },
        ]
        self.done = set([])

    def read(self):
        if self._filename is not None:
            f = codecs.open(self._filename, 'r', 'cp1252')
            for line in f.read().split('\n')[:-1]:
                if line[0] not in ['[',';']: # Skip comments
                    self.parse(line)

    def parse(self, line):
        elements = line.split('|')
        recordtype, versionnumber, imexplicit, data_owner_code = elements[0:4]
        if imexplicit == 'I':
            implicit = 'true'
        else:
            implicit = 'false'

        self._processors[recordtype].parse(recordtype, versionnumber, implicit, data_owner_code, elements[4:])
        self.done.add(recordtype)

    def type2create(self, name, types, references):
        output = 'CREATE TABLE %s (' % (name)
        attributes = []
        primarykeys = []
        foreignkeys = []
        for attribute in types:
            if attribute['type'] == 'N':
                part = '%s %s(%d)'%(attribute['name'], 'NUMERIC', attribute['length'])
            elif attribute['type'] == 'A':
                part = '%s %s(%d)'%(attribute['name'], 'VARCHAR', attribute['length'])
            elif attribute['type'] == 'B':
                part = '%s %s'%(attribute['name'], 'BOOLEAN')
            elif attribute['type'] == 'S':
                part = '%s %s'%(attribute['name'], 'SMALLINT')
            elif attribute['type'] == 'D':
                part = '%s %s'%(attribute['name'], 'DATE')
            elif attribute['type'] == 'T':
                part = '%s %s'%(attribute['name'], 'TIMESTAMP')
            elif attribute['type'] == 'TS':
                part = '%s %s'%(attribute['name'], 'TIMESTAMP')

            if attribute['aard'] != 'o':
                part += ' NOT NULL'

            if attribute['aard'] == '#':
                primarykeys.append(attribute['name'])

            attributes.append(part)

        if len(primarykeys) > 0:
            attributes.append('PRIMARY KEY (' + ', '.join(primarykeys) + ')')

        if references is not None:
            for table, keys in references.items():
                if type(keys) == tuple:
                    attributes.append('FOREIGN KEY (%s) REFERENCES %s(%s)' % (keys[0], table, keys[1]))
                else:
                    attributes.append('FOREIGN KEY (DataOwnerCode, %s) REFERENCES %s' % (', '.join(keys), table))

        output += ', '.join(attributes)
        output += ');'
        return output

    def write_part(self, table, data):
        if not os.path.exists ('tsv'):
            os.makedirs('tsv')
        f = codecs.open('tsv/%s.tsv'%(table), 'w', 'UTF-8')

        # Write to database
        try:
            connection = psycopg2.connect(user=sql_username,
                                        password=sql_password,
                                        host=sql_hostname,
                                        port=sql_port,
                                        database=sql_database)

            cursor = connection.cursor()

            # Delete data if exists
            delete_params = (table, sys.argv[1].lower())
            delete_sourcefile = """DELETE FROM %s WHERE sourcefile = '%s'""" % delete_params
            if delete_sourcefile and delete_params:
                cursor.execute(delete_sourcefile)
                connection.commit()

            # Executing a SQL query to insert datetime into table
            insert_query = ''
            insert_params = ()
            insert_query += """INSERT INTO %s (%s)""" % (table, helper.column(table))
            insert_query += """ VALUES (%s)""" % (helper.n_field(table))
                
            for i in range(len(data)):
                print 'LINE {iter} TABLE {table}'.format(iter = i, table = table)
                line = data[i]

                # Insert multiple data to database
                if i > 0:
                    insert_query += ", (%s)" % (helper.n_field(table))

                line.append(sys.argv[1].lower())
                f.write(';'.join(line)+'\n')

                line = [None if j == '' else j.encode('utf-8') for j in line]
                # Add sourcefile to tuple
                insert_params += tuple(line)
                
            if insert_query and insert_params:
                cursor.execute(insert_query, insert_params)
                connection.commit()
            
            f.close()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print "COPY %d RECORDS INTO %s FROM '%s/tsv/%s.tsv' DELIMITERS ';', '\\n' NULL AS '';" % (len(data), table, os.getcwd(), table)
                print("=================== PostgreSQL connection is closed ===================")

    def write(self):
        for x in self.done:
            print self.type2create(x.lower(), self.types + self._processors[x].types, self._processors[x].references)
            self.write_part(x.lower(), self._processors[x].data)

if __name__ == '__main__':
    if sys.argv[1].lower().endswith('.zip'):
        if not os.path.exists ('tmp'):
            os.makedirs('tmp')
        zf = zipfile.ZipFile(sys.argv[1])
        zf.extractall('tmp')

        start_time = time.time()

        for filename in zf.namelist():
            path = 'tmp/%s'%filename
            t = tmi(path)
            t.read()
            t.write()
        
        print("--- %s seconds ---" % (time.time() - start_time))

    else:
        t = tmi(sys.argv[1])
        t.read()
        t.write()
