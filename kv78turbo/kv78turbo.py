import sys
import time
import zmq
import codecs
import csv
import os
from const import ZMQ_KV8, ZMQ_KV78DEMO
from ctx import ctx, ctx_kv7
from datetime import datetime, timedelta
from gzip import GzipFile
from cStringIO import StringIO
import function
import psycopg2
from psycopg2.extensions import AsIs
import pandas as pd

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

tpc_store = {}
line_store = {}
journey_store = {}

tpc_meta = {}

f = codecs.open('stops.txt', 'r', 'utf-8')
reader = csv.reader(utf_8_encoder(f))
for row in reader:
    try:
        tpc, name, town, x, y = row
        tpc_meta[tpc] = {'Name': name, 'Town': town, 'X': float(x), 'Y': float(y)}
    except:
        pass
f.close()

def toisotime(operationdate, timestamp, row):
    hours, minutes, seconds = timestamp.split(':')
    hours = int(hours)
    if hours >= 48:
        print(row)

    if hours >= 24:
        deltadays  = hours / 24
        hours = hours % 24
        years, months, days = operationdate.split('-')
        return (datetime(int(years), int(months), int(days), hours, int(minutes), int(seconds)) + timedelta(days = deltadays)).isoformat()
    else:
        return operationdate+'T'+timestamp

def cleanup():
    now = datetime.today() + timedelta(seconds=120)
    for timingpointcode, values in tpc_store.items():
        for journey, row in values.items():
            if now > datetime.strptime(row['ExpectedArrivalTime'], "%Y-%m-%dT%H:%M:%S") and now > datetime.strptime(row['ExpectedDepartureTime'], "%Y-%m-%dT%H:%M:%S"):
                del(tpc_store[timingpointcode][journey])

    for journey_id, values in journey_store.items():
        row = values[max(values.keys())]
        if now > datetime.strptime(row['ExpectedArrivalTime'], "%Y-%m-%dT%H:%M:%S") and now > datetime.strptime(row['ExpectedArrivalTime'], "%Y-%m-%dT%H:%M:%S"):
            line_id = row['DataOwnerCode'] + '_' + row['LinePlanningNumber'] + '_' + row['LineDirection']

            if line_id in line_store and journey_id in line_store[line_id]['Actuals']:
                del(line_store[line_id]['Actuals'][journey_id])

            if journey_id in journey_store:
                del(journey_store[journey_id])

def storecurrect(row):
    id = '_'.join([row['DataOwnerCode'], row['LocalServiceLevelCode'], row['LinePlanningNumber'], row['JourneyNumber'], row['FortifyOrderNumber']])
    line_id = row['DataOwnerCode'] + '_' + row['LinePlanningNumber'] + '_' + row['LineDirection']

    row['ExpectedArrivalTime'] = toisotime(row['OperationDate'], row['ExpectedArrivalTime'], row)
    row['ExpectedDepartureTime'] = toisotime(row['OperationDate'], row['ExpectedDepartureTime'], row)
    
    try:
        for x in ['JourneyNumber', 'FortifyOrderNumber', 'UserStopOrderNumber', 'NumberOfCoaches', 'VehicleNumber']:
            if x not in row:
                row[x] = None
            if x in row and row[x] is not None and row[x] != 'UNKNOWN':
                row[x] = int(row[x])
        row['IsTimingStop'] = (row['IsTimingStop'] == '1')
    except:
        raise

    if line_id not in line_store:
        line_store[line_id] = { 'DataOwnerCode': row['DataOwnerCode'], 'Network': {}, 'Actuals': {} }
    
    if row['UserStopOrderNumber'] not in line_store[line_id]['Network']:
        line_store[line_id]['Network'][row['UserStopOrderNumber']] = {
            'TimingPointCode': row['TimingPointCode'],
            'IsTimingStop': row['IsTimingStop']
            }
        if row['TimingPointCode'] in tpc_meta:
            line_store[line_id]['Network'][row['UserStopOrderNumber']].update(tpc_meta[row['TimingPointCode']])

    if id not in journey_store:
        journey_store[id] = {row['UserStopOrderNumber']: row}
    else:
        journey_store[id][row['UserStopOrderNumber']] = row

    if row['TripStopStatus'] in set(['ARRIVED', 'PASSED']): # , 'DRIVING']): Driving alleen nemen als kleinste waarde uit lijn, gegeven dat er geen ARRIVED/PASSED is
        for key in journey_store[id].keys():
            if key < row['UserStopOrderNumber']:
                del(journey_store[id][key])

        if row['JourneyStopType'] == 'LAST':
            if id in line_store[line_id]['Actuals']:
                del line_store[line_id]['Actuals'][id]
        else:
            line_store[line_id]['Actuals'][id] = row

    if row['TimingPointCode'] not in tpc_store:
        tpc_store[row['TimingPointCode']] = {id: row}
    else:
        tpc_store[row['TimingPointCode']][id] = row

def copy_table(cursor, connection, c, table, keys):
    prefix = 'kv7_'
    if table in c.ctx:
        column = keys
        # values = [tuple(c.ctx[table].rows()[i].values()) for i in range(0, len(c.ctx[table].rows()))]
        values = [c.ctx[table].columns()[column] for column in column]
        df = pd.DataFrame(values).T
        values = df.to_records(index=False)
        values = [tuple(values[i]) for i in range (len(values))]
        table = prefix + table.lower()
        
        insert_tmp = """INSERT INTO tmp_%s (%s) values (%s)""" % (table, ','.join(x.lower() for x in keys), function.type_data(table))
        cursor.executemany(insert_tmp, values)
        connection.commit()

        insert_data = """INSERT INTO %s SELECT * FROM tmp_%s EXCEPT SELECT * FROM %s;""" % (table, table, table)
        cursor.execute(insert_data)
        connection.commit()

        del_tmp = """DELETE FROM tmp_%s;""" % (table)
        cursor.execute(del_tmp)
        connection.commit()

def KV7kalender(cursor, connection, contents):
    c = ctx_kv7(contents)
    copy_table(cursor, connection, c, 'LOCALSERVICEGROUP', ['DataOwnerCode', 'LocalServiceLevelCode'])
    copy_table(cursor, connection, c, 'LOCALSERVICEGROUPVALIDITY', ['DataOwnerCode', 'LocalServiceLevelCode', 'OperationDate'])

def KV7planning(cursor, connection, contents):
    c = ctx_kv7(contents)
    # copy_table(cursor, connection, c, 'LINE', ['DataOwnerCode', 'LinePlanningNumber', 'LinePublicNumber', 'LineName', 'LineVeTagNumber', 'TransportType'])
    # copy_table(cursor, connection, c, 'DESTINATION', ['DataOwnerCode', 'DestinationCode', 'DestinationName50', 'DestinationName30','DestinationName24','DestinationName19','DestinationName16','DestinationDetail24', 'DestinationDetail19', 'DestinationDetail16', 'DestinationDisplay16'])
    # copy_table(cursor, connection, c, 'DESTINATIONVIA', ['DataOwnerCode', 'DestinationCodeP', 'DestinationCodeC', 'DestinationViaOrderNr'])
    # copy_table(cursor, connection, c, 'TIMINGPOINT', ['DataOwnerCode', 'TimingPointCode', 'TimingPointName', 'TimingPointTown', 'StopAreaCode'])
    # copy_table(cursor, connection, c, 'USERTIMINGPOINT', ['DataOwnerCode', 'UserStopCode', 'TimingPointDataOwnerCode', 'TimingPointCode'])
    copy_table(cursor, connection, c, 'LOCALSERVICEGROUPPASSTIME', ['DataOwnerCode', 'LocalServiceLevelCode', 'LinePlanningNumber', 'JourneyNumber', 'FortifyOrderNumber','UserStopCode','UserStopOrderNumber','LineDirection','DestinationCode','TargetArrivalTime','TargetDepartureTime','SideCode','WheelChairAccessible','JourneyStopType','IsTimingStop','ProductFormulaType'])


context = zmq.Context()

kv8 = context.socket(zmq.SUB)
kv8.connect("tcp://pubsub.besteffort.ndovloket.nl:7817")
kv8.setsockopt(zmq.SUBSCRIBE, "/GOVI/KV8passtimes/CXX")

kv7 = context.socket(zmq.SUB)
kv7.connect("tcp://pubsub.besteffort.ndovloket.nl:7817")
kv7.setsockopt(zmq.SUBSCRIBE, "/GOVI/KV7calendar")
kv7.setsockopt(zmq.SUBSCRIBE, "/GOVI/KV7planning")

# client = context.socket(zmq.REP)
# client.bind(ZMQ_KV78DEMO)

poller = zmq.Poller()
# poller.register(client, zmq.POLLIN)
poller.register(kv7, zmq.POLLIN)
poller.register(kv8, zmq.POLLIN)

garbage = 0

csv_kv8_pt = "parse_data/kv8_pt.csv" # kv8 datedpasstime
csv_kv7_lsg = "parse_data/kv7_lsg.csv" # kv7 localservicegroup
csv_kv7_lsgv = "parse_data/kv7_lsgv.csv" # kv7 localservicegroupvalidity
csv_kv7_do = "parse_data/kv7_do.csv" # kv7 dataowner
csv_kv7_lsgpt = "parse_data/kv7_lsgpt.csv" # kv7 localservicegrouppasstime
csv_kv7_l = "parse_data/kv7_l.csv" # kv7 line
csv_kv7_utp = "parse_data/kv7_utp.csv" # kv7 usertimingpoint
csv_kv7_tp = "parse_data/kv7_tp.csv" # kv7 timingpoint
csv_kv7_sa = "parse_data/kv7_sa.csv" # kv7 stoparea
csv_kv7_d = "parse_data/kv7_d.csv" # kv7 destination
csv_kv7_dv = "parse_data/kv7_dv.csv" # kv7 destinationvia

# Connection to database
connection = psycopg2.connect(
    user="postgres",
    password="Maestronic123",
    host="localhost",
    port=5432,
    database="netex_timetable")
cursor = connection.cursor()

# # Dump KV7 calendar data
# f = open("kv7calendardata/CXX").read()
# c = ctx_kv7(f)

# if 'LOCALSERVICEGROUP' in c.ctx:
#     counter = 1
#     for row in c.ctx['LOCALSERVICEGROUP'].rows():
#         new_row = function.normalize_kv7_lsg(row, counter)
#         try:
#             with open(csv_kv7_lsg, 'ab') as csvfile:
#                 writer = csv.DictWriter(csvfile, new_row.keys())
#                 if (counter == 1):
#                     writer.writeheader()
#                 counter += 1
#                 writer.writerow(new_row)
#         except IOError:
#             print("I/O error")

# if 'LOCALSERVICEGROUPVALIDITY' in c.ctx:
#     counter = 1
#     for row in c.ctx['LOCALSERVICEGROUPVALIDITY'].rows():
#         new_row = function.normalize_kv7_lsgv(row, counter)
#         try:
#             with open(csv_kv7_lsgv, 'ab') as csvfile:
#                 writer = csv.DictWriter(csvfile, new_row.keys())
#                 if (counter == 1):
#                     writer.writeheader()
#                 counter += 1
#                 writer.writerow(new_row)
#         except IOError:
#             print("I/O error")

# # Dump KV7 planning data
# files = os.listdir('kv7planningdata/')
# for entry in files:
#     f = open("kv7planningdata/"+entry).read()
#     c = ctx_kv7(f)

#     if 'STOPAREA' in c.ctx:
#         counter = 1
#         for row in c.ctx['STOPAREA'].rows():
#             new_row = function.normalize_kv7_sa(row, counter)
#             try:
#                 with open('parse_data/kv7_sa_%s.csv' % (entry), 'ab') as csvfile:
#                     writer = csv.DictWriter(csvfile, new_row.keys())
#                     if (counter == 1):
#                         writer.writeheader()
#                     counter += 1
#                     writer.writerow(new_row)
#             except IOError:
#                 print("I/O error")

#     if 'DATAOWNER' in c.ctx:
#         counter = 1
#         for row in c.ctx['DATAOWNER'].rows():
#             new_row = function.normalize_kv7_do(row, counter)
#             try:
#                 with open('parse_data/kv7_do_%s.csv' % (entry), 'ab') as csvfile:
#                     writer = csv.DictWriter(csvfile, new_row.keys())
#                     if (counter == 1):
#                         writer.writeheader()
#                     counter += 1
#                     writer.writerow(new_row)
#             except IOError:
#                 print("I/O error")

#     if 'DESTINATION' in c.ctx:
#         counter = 1
#         for row in c.ctx['DESTINATION'].rows():
#             new_row = function.normalize_kv7_d(row, counter)
#             try:
#                 with open('parse_data/kv7_d_%s.csv' % (entry), 'ab') as csvfile:
#                     writer = csv.DictWriter(csvfile, new_row.keys())
#                     if (counter == 1):
#                         writer.writeheader()
#                     counter += 1
#                     writer.writerow(new_row)
#             except IOError:
#                 print("I/O error")

#     if 'USERTIMINGPOINT' in c.ctx:
#         counter = 1
#         for row in c.ctx['USERTIMINGPOINT'].rows():
#             new_row = function.normalize_kv7_utp(row, counter)
#             try:
#                 with open('parse_data/kv7_utp_%s.csv' % (entry), 'ab') as csvfile:
#                     writer = csv.DictWriter(csvfile, new_row.keys())
#                     if (counter == 1):
#                         writer.writeheader()
#                     counter += 1
#                     writer.writerow(new_row)
#             except IOError:
#                 print("I/O error")

#     if 'LINE' in c.ctx:
#         counter = 1
#         for row in c.ctx['LINE'].rows():
#             new_row = function.normalize_kv7_l(row, counter)
#             try:
#                 with open('parse_data/kv7_l_%s.csv' % (entry), 'ab') as csvfile:
#                     writer = csv.DictWriter(csvfile, new_row.keys())
#                     if (counter == 1):
#                         writer.writeheader()
#                     counter += 1
#                     writer.writerow(new_row)
#             except IOError:
#                 print("I/O error")

#     if 'LOCALSERVICEGROUPPASSTIME' in c.ctx:
#         counter = 1
#         for row in c.ctx['LOCALSERVICEGROUPPASSTIME'].rows():
#             new_row = function.normalize_kv7_lsgpt(row, counter)
#             try:
#                 with open('parse_data/kv7_lsgpt_%s.csv' % (entry), 'ab') as csvfile:
#                     writer = csv.DictWriter(csvfile, new_row.keys())
#                     if (counter == 1):
#                         writer.writeheader()
#                     counter += 1
#                     writer.writerow(new_row)
#             except IOError:
#                 print("I/O error")

#     if 'TIMINGPOINT' in c.ctx:
#         counter = 1
#         for row in c.ctx['TIMINGPOINT'].rows():
#             new_row = function.normalize_kv7_tp(row, counter)
#             try:
#                 with open('parse_data/kv7_tp_%s.csv' % (entry), 'ab') as csvfile:
#                     writer = csv.DictWriter(csvfile, new_row.keys())
#                     if (counter == 1):
#                         writer.writeheader()
#                     counter += 1
#                     writer.writerow(new_row)
#             except IOError:
#                 print("I/O error")

# # Dump KV7 with database
# clear = True
# if clear:
#     cursor.execute(function.drop_table())
#     cursor.execute(function.main_table())

# cursor.execute("START TRANSACTION;")
# cursor.execute(function.tmp_table())
# connection.commit()

# dir_kv7planning = 'kv7planningdata'
# dir_kv7calendar = 'kv7calendardata/CXX'

# for filename in os.listdir(dir_kv7planning):
#     # contents = codecs.open(dir_kv7planning + '/' + filename, 'r', 'UTF-8').read()
#     print filename
#     contents = open(dir_kv7planning + '/' + filename).read()
#     KV7planning(cursor, connection, contents)

# print dir_kv7calendar
# contents = open(dir_kv7calendar).read()
# KV7kalender(cursor, connection, contents)

# if (connection):
#     cursor.close()
#     connection.close()
#     print("=================== PostgreSQL connection is closed ===================")

# Initial counter
counter = 1
while True:
    socks = dict(poller.poll())
    
    if socks.get(kv8) == zmq.POLLIN:
        multipart = kv8.recv_multipart()
        content = GzipFile('','r',0,StringIO(''.join(multipart[1:]))).read()
        c = ctx(content)
        # if 'DATEDPASSTIME' in c.ctx:
        #     for row in c.ctx['DATEDPASSTIME'].rows():
        #         storecurrect(row)
        #         new_row = function.normalize_kv8_pt(row, counter)
        #         try:
        #             with open(csv_kv8_pt, 'ab') as csvfile:
        #                 writer = csv.DictWriter(csvfile, new_row.keys())
        #                 if (counter == 1):
        #                     writer.writeheader()
        #                 counter += 1
        #                 writer.writerow(new_row)
        #         except IOError:
        #             print("I/O error")
    
    elif socks.get(kv7) == zmq.POLLIN:
        multipart = kv7.recv_multipart()
        content = GzipFile('','r',0,StringIO(''.join(multipart[1:]))).read()
        c = ctx_kv7(content)
        print(c.ctx)
        if 'LOCALSERVICEGROUP' in c.ctx:
            counter = 1
            for row in c.ctx['LOCALSERVICEGROUP'].rows():
                new_row = function.normalize_kv7_lsg(row, counter)
                try:
                    with open(csv_kv7_lsg, 'ab') as csvfile:
                        writer = csv.DictWriter(csvfile, new_row.keys())
                        if (counter == 1):
                            writer.writeheader()
                        counter += 1
                        writer.writerow(new_row)
                except IOError:
                    print("I/O error")

        if 'LOCALSERVICEGROUPVALIDITY' in c.ctx:
            counter = 1
            for row in c.ctx['LOCALSERVICEGROUPVALIDITY'].rows():
                new_row = function.normalize_kv7_lsgv(row, counter)
                try:
                    with open(csv_kv7_lsgv, 'ab') as csvfile:
                        writer = csv.DictWriter(csvfile, new_row.keys())
                        if (counter == 1):
                            writer.writeheader()
                        counter += 1
                        writer.writerow(new_row)
                except IOError:
                    print("I/O error")

        if 'STOPAREA' in c.ctx:
            counter = 1
            for row in c.ctx['STOPAREA'].rows():
                new_row = function.normalize_kv7_sa(row, counter)
                try:
                    with open(csv_kv7_sa, 'ab') as csvfile:
                        writer = csv.DictWriter(csvfile, new_row.keys())
                        if (counter == 1):
                            writer.writeheader()
                        counter += 1
                        writer.writerow(new_row)
                except IOError:
                    print("I/O error")

        if 'DATAOWNER' in c.ctx:
            counter = 1
            for row in c.ctx['DATAOWNER'].rows():
                new_row = function.normalize_kv7_do(row, counter)
                try:
                    with open(csv_kv7_do, 'ab') as csvfile:
                        writer = csv.DictWriter(csvfile, new_row.keys())
                        if (counter == 1):
                            writer.writeheader()
                        counter += 1
                        writer.writerow(new_row)
                except IOError:
                    print("I/O error")

        if 'DESTINATION' in c.ctx:
            counter = 1
            for row in c.ctx['DESTINATION'].rows():
                new_row = function.normalize_kv7_d(row, counter)
                try:
                    with open(csv_kv7_d, 'ab') as csvfile:
                        writer = csv.DictWriter(csvfile, new_row.keys())
                        if (counter == 1):
                            writer.writeheader()
                        counter += 1
                        writer.writerow(new_row)
                except IOError:
                    print("I/O error")

        if 'USERTIMINGPOINT' in c.ctx:
            counter = 1
            for row in c.ctx['USERTIMINGPOINT'].rows():
                new_row = function.normalize_kv7_utp(row, counter)
                try:
                    with open(csv_kv7_utp, 'ab') as csvfile:
                        writer = csv.DictWriter(csvfile, new_row.keys())
                        if (counter == 1):
                            writer.writeheader()
                        counter += 1
                        writer.writerow(new_row)
                except IOError:
                    print("I/O error")

        if 'LINE' in c.ctx:
            counter = 1
            for row in c.ctx['LINE'].rows():
                new_row = function.normalize_kv7_l(row, counter)
                try:
                    with open(csv_kv7_l, 'ab') as csvfile:
                        writer = csv.DictWriter(csvfile, new_row.keys())
                        if (counter == 1):
                            writer.writeheader()
                        counter += 1
                        writer.writerow(new_row)
                except IOError:
                    print("I/O error")

        if 'LOCALSERVICEGROUPPASSTIME' in c.ctx:
            counter = 1
            for row in c.ctx['LOCALSERVICEGROUPPASSTIME'].rows():
                new_row = function.normalize_kv7_lsgpt(row, counter)
                try:
                    with open(csv_kv7_lsgpt, 'ab') as csvfile:
                        writer = csv.DictWriter(csvfile, new_row.keys())
                        if (counter == 1):
                            writer.writeheader()
                        counter += 1
                        writer.writerow(new_row)
                except IOError:
                    print("I/O error")

        if 'TIMINGPOINT' in c.ctx:
            counter = 1
            for row in c.ctx['TIMINGPOINT'].rows():
                new_row = function.normalize_kv7_tp(row, counter)
                try:
                    with open(csv_kv7_tp, 'ab') as csvfile:
                        writer = csv.DictWriter(csvfile, new_row.keys())
                        if (counter == 1):
                            writer.writeheader()
                        counter += 1
                        writer.writerow(new_row)
                except IOError:
                    print("I/O error")

    if garbage > 120:
        cleanup()
        garbage = 0
    else:
        garbage += 1
