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
            'FINANCER': tmi_financer(),
            'CONFINREL': tmi_confinrel(),
            'ICON': tmi_icon(),
            'DEST': tmi_dest(),
            'EXCOPDAY': tmi_excopday(),
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
            {'name': 'Version', 'aard': 'x', 'type': 'N', 'length': 2 },
            {'name': 'Implicit', 'aard': 'x', 'type': 'B', 'length': 1 },
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

        self._processors[recordtype].parse(versionnumber, implicit, data_owner_code, elements[4:])
        self.done.add(recordtype)

    def type2create(self, name, types, references):
        output = 'CREATE TABLE %s (' % (name)
        attributes = []
        primarykeys = []
        foreignkeys = []
        header = []
        for attribute in types:
            header.append(attribute['name'])
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
                part = '%s %s'%(attribute['name'], 'TIME')
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
                    attributes.append('FOREIGN KEY (DataOwnerCode, %s) REFERENCES %s' % (', '.join(map(str, keys)), table))

        output += ', '.join(attributes)
        output += ');'
        return output, header

    def write_part(self, table, data, cursor, connection, header):
        if not os.path.exists ('csv'):
            os.makedirs('csv')
        f = codecs.open('csv/%s.csv'%(table), 'w', 'UTF-8')
        f.write(';'.join(header)+'\n')
        for line in data:
            f.write(';'.join(line)+'\n')
        f.close()

        import_query = """COPY %s FROM '%s/csv/%s.csv' WITH (FORMAT csv, NULL '', DELIMITER ';', HEADER);""" % (table, os.getcwd(), table)
        print import_query
        if import_query:
            cursor.execute(import_query)
            connection.commit()

    def write(self, cursor, connection):
        for x in self.done:
            create_query, header = self.type2create(x.lower(), self.types + self._processors[x].types, self._processors[x].references)
            print create_query
            if create_query:
                cursor.execute(create_query)
                connection.commit()

            self.write_part(x.lower(), self._processors[x].data, cursor, connection, header)

if __name__ == '__main__':
    start_time = time.time()
    try:
        connection = psycopg2.connect(user=sql_username,
                                    password=sql_password,
                                    host=sql_hostname,
                                    port=sql_port,
                                    database=sql_database)

        cursor = connection.cursor()
        if sys.argv[1].lower().endswith('.zip'):
            if not os.path.exists ('tmp'):
                os.makedirs('tmp')
            zf = zipfile.ZipFile(sys.argv[1])
            zf.extractall('tmp')

            # Drop table in database
            drop_query = """DROP SCHEMA public CASCADE;
                            CREATE SCHEMA public;

                            GRANT ALL ON SCHEMA public TO postgres;
                            GRANT ALL ON SCHEMA public TO public;"""
            if drop_query:
                cursor.execute(drop_query)
                connection.commit()
            
            for filename in helper.table_order():
                path = 'tmp/%s.TMI' % filename
                t = tmi(path)
                if os.path.exists (path):
                    t.read()
                else:
                    t.done.add(filename)
                t.write(cursor, connection)

        else:
            t = tmi(sys.argv[1])
            t.read()
            t.write(cursor, connection)
    
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("=================== PostgreSQL connection is closed ===================")
    
    print("--- %s seconds ---" % (time.time() - start_time))