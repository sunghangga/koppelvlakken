def time32(timestamp32):
    hour, minute, second = timestamp32.split(':')
    hour = int(hour)
    if hour > 23:
        hour -= 24
        return '1970-01-02T%.2d:%s:%s'%(hour, minute, second)
    else:
        return '1970-01-01T'+timestamp32

def timeform(timestamp32):
    hour, minute, second = timestamp32.split(':')
    hour = int(hour)
    if hour > 23:
        hour -= 24
        return '%.2d:%s:%s'%(hour, minute, second)
    else:
        return timestamp32

def wheelchair(wheel_chair_accessible):
    if (wheel_chair_accessible == 'ACCESSIBLE'):
        wheel_chair_accessible = 'true'
    elif (wheel_chair_accessible == 'NOTACCESSIBLE'):
        wheel_chair_accessible = 'false'
    else:
        wheel_chair_accessible = ''

    return wheel_chair_accessible

def boolsql(boolean):
    if boolean:
        return 'true'
    else:
        return 'false'

def daytype2bitstring(daytype):
    return ('7' in daytype) * 2 ** 0 + \
           ('1' in daytype) * 2 ** 1 + \
           ('2' in daytype) * 2 ** 2 + \
           ('3' in daytype) * 2 ** 3 + \
           ('4' in daytype) * 2 ** 4 + \
           ('5' in daytype) * 2 ** 5 + \
           ('6' in daytype) * 2 ** 6

def day2int(daytype):
    return ('7' in daytype) * 7 + \
           ('1' in daytype) * 1 + \
           ('2' in daytype) * 2 + \
           ('3' in daytype) * 3 + \
           ('4' in daytype) * 4 + \
           ('5' in daytype) * 5 + \
           ('6' in daytype) * 6

def table_order():
    t_order = [
        'CONAREA', 
        'FINANCER', 
        'CONFINREL', 
        'ICON', 
        'DEST', 
        'SPECDAY',
        'PEGR',
        'EXCOPDAY', 
        'LINE',
        'JOPA', 
        'USRSTAR',
        'USRSTOP',
        'TILI',
        'JOPATILI',
        'LINK', 
        'NOTICE', 
        'ORUN',
        'TIVE',
        'TIMDEMGRP',
        'PUJO',
        'SCHEDVERS',
        'PUJOPASS',
        'NTCASSGNM', 
        'OPERDAY', 
        'ORUNORUN',
        'PEGRVAL', 
        'POINT', 
        'POOL',
        'TIMDEMRNT'
    ]
    return t_order

def column(table):
    if table == 'conarea':
        return 'recordtype, version, implicit, dataownercode, concessionareacode, description, sourcefile'
    elif table == 'confinrel':
        return 'recordtype, version, implicit, dataownercode, confinrelcode, concessionareacode, financercode, sourcefile'
    elif table == 'dest':
        return 'recordtype, version, implicit, dataownercode, destcode, destnamefull, destnamemain, destnamedetail, relevantdestnamedetail, destnamemain21, destnamedetail21, destnamemain19, destnamedetail19, destnamemain16, destnamedetail16, desticon, destcolor, sourcefile'
    elif table == 'excopday':
        return 'recordtype, version, implicit, dataownercode, organizationalunitcode, validdate, daytypeason, specificdaycode, periodgroupcode, description, sourcefile'
    elif table == 'financer':
        return 'recordtype, version, implicit, dataownercode, financercode, description, sourcefile'
    elif table == 'icon':
        return 'recordtype, version, implicit, dataownercode, iconnumber, iconuri, sourcefile'
    elif table == 'jopa':
        return 'recordtype, version, implicit, dataownercode, lineplanningnumber, journeypatterncode, journeypatterntype, direction, description, sourcefile'
    elif table == 'jopatili':
        return 'recordtype, version, implicit, dataownercode, lineplanningnumber, journeypatterncode, timinglinkorder, userstopcodebegin, userstopcodeend, confinrelcode, destcode, istimingstop, displaypublicline, productformulatype, getin, getout, showflexibletrip, linedesticon, linedestcolor, linedesttextcolor, sourcefile'
    elif table == 'line':
        return 'recordtype, version, implicit, dataownercode, lineplanningnumber, linepublicnumber, linename, linevetagnumber, description, transporttype, lineicon, linecolor, linetextcolor, sourcefile'
    elif table == 'link':
        return 'recordtype, version, implicit, dataownercode, userstopcodebegin, userstopcodeend, validfrom, distance, description, transporttype, sourcefile'
    elif table == 'notice':
        return 'recordtype, version, implicit, dataownercode, noticecode, noticecontent, sourcefile'
    elif table == 'ntcassgnm':
        return 'recordtype, version, implicit, dataownercode, noticecode, assignedobject, timetableversioncode, organizationalunitcode, schedulecode, scheduletypecode, periodgroupcode, specificdaycode, daytype, lineplanningnumber, journeynumber, stoporder, journeypatterncode, timinglinkorder, userstopcode, sourcefile'
    elif table == 'operday':
        return 'recordtype, version, implicit, dataownercode, organizationalunitcode, schedulecode, scheduletypecode, validdate, description'
    elif table == 'orun':
        return 'recordtype, version, implicit, dataownercode, organizationalunitcode, name, organizationalunittype, description, sourcefile'
    elif table == 'orunorun':
        return 'recordtype, version, implicit, dataownercode, organizationalunitcodeparent, organizationalunitcodechild, validfrom, sourcefile'
    elif table == 'pegr':
        return 'recordtype, version, implicit, dataownercode, periodgroupcode, description, sourcefile'
    elif table == 'pegrval':
        return 'recordtype, version, implicit, dataownercode, organizationalunitcode, periodgroupcode, validfrom, validthru, sourcefile'
    elif table == 'point':
        return 'recordtype, version, implicit, dataownercode, pointcode, validform, pointtype, coordinatesystemtype, locationx_ew, locationy_ns, localtionz, description, sourcefile'
    elif table == 'pool':
        return 'recordtype, version, implicit, dataownercode, userstopcodebegin, userstopcodeend, linkvalidfrom, pointdataownercode, pointcode, distancesincestartoflink, segmentspeed, localpointspeed, description, transporttype, sourcefile'
    elif table == 'pujo':
        return 'recordtype, version, implicit, dataownercode, timetableversioncode, organizationalunitcode, periodgroupcode, specificdaycode, daytype, lineplanningnumber, journeynumber, timedemandgroupcode, journeypatterncode, departuretime, wheelchairaccessible, dataownerisoperator, plannedmonitored, productformulatype, showflexibletrip, sourcefile'
    elif table == 'pujopass':
        return 'recordtype, version, implicit, dataownercode, organizationalunitcode, schedulecode, scheduletypecode, lineplanningnumber, journeynumber, stoporder, journeypatterncode, userstopcode, targetarrivaltime, targetdeparturetime, wheelchairaccessible, dataownerisoperator, sourcefile'
    elif table == 'schedvers':
        return 'recordtype, version, implicit, dataownercode, organizationalunitcode, schedulecode, scheduletypecode, validfrom, validthru, description, sourcefile'
    elif table == 'specday':
        return 'recordtype, version, implicit, dataownercode, specificdaycode, name, description, sourcefile'
    elif table == 'tili':
        return 'recordtype, version, implicit, dataownercode, userstopcodebegin, userstopcodeend, minimaldrivetime, description, sourcefile'
    elif table == 'timdemgrp':
        return 'recordtype, version, implicit, dataownercode, lineplanningnumber, journeypatterncode, timedemandgroupcode, sourcefile'
    elif table == 'timdemrnt':
        return 'recordtype, version, implicit, dataownercode, lineplanningnumber, journeypatterncode, timedemandgroupcode, timinglinkorder, userstopcodebegin, userstopcodeend, totaldrivetime, drivetime, expecteddelay, layovertime, stopwaittime, minimumstoptime, sourcefile'
    elif table == 'tive':
        return 'recordtype, version, implicit, dataownercode, organizationalunitcode, timetableversioncode, periodgroupcode, specificdaycode, validfrom, timetableversiontype, validthru, description, sourcefile'
    elif table == 'usrstar':
        return 'recordtype, version, implicit, dataownercode, userstopareacode, name, town, roadsideeqdataownercode, roadsideequnitnumber, description, sourcefile'
    elif table == 'usrstop':
        return 'recordtype, version, implicit, dataownercode, userstopcode, timingpointcode, getin, getout, name, town, userstopareacode, stopsidecode, roadsideeqdataownercode, roadsideequnitnumber, minimalstoptime, stopsidelength, description, userstoptype, quaycode, sourcefile'
    else:
        return ''

def column_form(table):
    if table == 'conarea':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'concessionareacode', 'description', 'sourcefile'
    elif table == 'confinrel':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'confinrelcode', 'concessionareacode', 'financercode', 'sourcefile'
    elif table == 'dest':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'destcode', 'destnamefull', 'destnamemain', 'destnamedetail', 'relevantdestnamedetail', 'destnamemain21', 'destnamedetail21', 'destnamemain19', 'destnamedetail19', 'destnamemain16', 'destnamedetail16', 'desticon', 'destcolor', 'sourcefile'
    elif table == 'excopday':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'organizationalunitcode', 'validdate', 'daytypeason', 'specificdaycode', 'periodgroupcode', 'description', 'sourcefile'
    elif table == 'financer':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'financercode', 'description', 'sourcefile'
    elif table == 'icon':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'iconnumber', 'iconuri', 'sourcefile'
    elif table == 'jopa':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'lineplanningnumber', 'journeypatterncode', 'journeypatterntype', 'direction', 'description', 'sourcefile'
    elif table == 'jopatili':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'lineplanningnumber', 'journeypatterncode', 'timinglinkorder', 'userstopcodebegin', 'userstopcodeend', 'confinrelcode', 'destcode', 'istimingstop', 'displaypublicline', 'productformulatype', 'getin', 'getout', 'showflexibletrip', 'linedesticon', 'linedestcolor', 'linedesttextcolor', 'sourcefile'
    elif table == 'line':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'lineplanningnumber', 'linepublicnumber', 'linename', 'linevetagnumber', 'description', 'transporttype', 'lineicon', 'linecolor', 'linetextcolor', 'sourcefile'
    elif table == 'link':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'userstopcodebegin', 'userstopcodeend', 'validfrom', 'distance', 'description', 'transporttype', 'sourcefile'
    elif table == 'notice':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'noticecode', 'noticecontent', 'sourcefile'
    elif table == 'ntcassgnm':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'noticecode', 'assignedobject', 'timetableversioncode', 'organizationalunitcode', 'schedulecode', 'scheduletypecode', 'periodgroupcode', 'specificdaycode', 'daytype', 'lineplanningnumber', 'journeynumber', 'stoporder', 'journeypatterncode', 'timinglinkorder', 'userstopcode', 'sourcefile'
    elif table == 'operday':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'organizationalunitcode', 'schedulecode', 'scheduletypecode', 'validdate', 'description'
    elif table == 'orun':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'organizationalunitcode', 'name', 'organizationalunittype', 'description', 'sourcefile'
    elif table == 'orunorun':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'organizationalunitcodeparent', 'organizationalunitcodechild', 'validfrom', 'sourcefile'
    elif table == 'pegr':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'periodgroupcode', 'description', 'sourcefile'
    elif table == 'pegrval':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'organizationalunitcode', 'periodgroupcode', 'validfrom', 'validthru', 'sourcefile'
    elif table == 'point':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'pointcode', 'validform', 'pointtype', 'coordinatesystemtype', 'locationx_ew', 'locationy_ns', 'localtionz', 'description', 'sourcefile'
    elif table == 'pool':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'userstopcodebegin', 'userstopcodeend', 'linkvalidfrom', 'pointdataownercode', 'pointcode', 'distancesincestartoflink', 'segmentspeed', 'localpointspeed', 'description', 'transporttype', 'sourcefile'
    elif table == 'pujo':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'timetableversioncode', 'organizationalunitcode', 'periodgroupcode', 'specificdaycode', 'daytype', 'lineplanningnumber', 'journeynumber', 'timedemandgroupcode', 'journeypatterncode', 'departuretime', 'wheelchairaccessible', 'dataownerisoperator', 'plannedmonitored', 'productformulatype', 'showflexibletrip', 'sourcefile'
    elif table == 'pujopass':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'organizationalunitcode', 'schedulecode', 'scheduletypecode', 'lineplanningnumber', 'journeynumber', 'stoporder', 'journeypatterncode', 'userstopcode', 'targetarrivaltime', 'targetdeparturetime', 'wheelchairaccessible', 'dataownerisoperator', 'sourcefile'
    elif table == 'schedvers':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'organizationalunitcode', 'schedulecode', 'scheduletypecode', 'validfrom', 'validthru', 'description', 'sourcefile'
    elif table == 'specday':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'specificdaycode', 'name', 'description', 'sourcefile'
    elif table == 'tili':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'userstopcodebegin', 'userstopcodeend', 'minimaldrivetime', 'description', 'sourcefile'
    elif table == 'timdemgrp':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'lineplanningnumber', 'journeypatterncode', 'timedemandgroupcode', 'sourcefile'
    elif table == 'timdemrnt':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'lineplanningnumber', 'journeypatterncode', 'timedemandgroupcode', 'timinglinkorder', 'userstopcodebegin', 'userstopcodeend', 'totaldrivetime', 'drivetime', 'expecteddelay', 'layovertime', 'stopwaittime', 'minimumstoptime', 'sourcefile'
    elif table == 'tive':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'organizationalunitcode', 'timetableversioncode', 'periodgroupcode', 'specificdaycode', 'validfrom', 'timetableversiontype', 'validthru', 'description', 'sourcefile'
    elif table == 'usrstar':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'userstopareacode', 'name', 'town', 'roadsideeqdataownercode', 'roadsideequnitnumber', 'description', 'sourcefile'
    elif table == 'usrstop':
        return 'recordtype', 'version', 'implicit', 'dataownercode', 'userstopcode', 'timingpointcode', 'getin', 'getout', 'name', 'town', 'userstopareacode', 'stopsidecode', 'roadsideeqdataownercode', 'roadsideequnitnumber', 'minimalstoptime', 'stopsidelength', 'description', 'userstoptype', 'quaycode', 'sourcefile'
    else:
        return ''

def n_field(table):
    if table == 'conarea':
        return '%s, %s, %s, %s, %s, %s, %s'
    elif table == 'confinrel':
        return '%s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'dest':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'excopday':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'financer':
        return '%s, %s, %s, %s, %s, %s, %s'
    elif table == 'icon':
        return '%s, %s, %s, %s, %s, %s, %s'
    elif table == 'jopa':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'jopatili':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'line':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'link':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'notice':
        return '%s, %s, %s, %s, %s, %s, %s'
    elif table == 'ntcassgnm':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'operday':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'orun':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'orunorun':
        return '%s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'pegr':
        return '%s, %s, %s, %s, %s, %s, %s'
    elif table == 'pegrval':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'point':
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"
    elif table == 'pool':
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"
    elif table == 'pujo':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'pujopass':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'schedvers':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'specday':
        return '%s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'tili':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'timdemgrp':
        return '%s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'timdemrnt':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'tive':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'usrstar':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    elif table == 'usrstop':
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
    else:
        return ''