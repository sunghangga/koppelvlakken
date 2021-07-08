def normalize_kv8_pt(row, counter):
    new_row = {}
    # new_row['id'] = counter
    new_row['DataOwnerCode'] = row['DataOwnerCode']
    new_row['OperationDate'] = row['OperationDate']
    new_row['LinePlanningNumber'] = row['LinePlanningNumber']
    new_row['JourneyNumber'] = row['JourneyNumber']
    new_row['FortifyOrderNumber'] = row['FortifyOrderNumber']
    new_row['UserStopOrderNumber'] = row['UserStopOrderNumber']
    new_row['UserStopCode'] = row['UserStopCode']
    new_row['LocalServiceLevelCode'] = row['LocalServiceLevelCode']
    new_row['LineDirection'] = row['LineDirection']
    new_row['LastUpdateTimeStamp'] = row['LastUpdateTimeStamp']
    new_row['DestinationCode'] = row['DestinationCode']
    new_row['IsTimingStop'] = row['IsTimingStop']
    new_row['ExpectedArrivalTime'] = row['ExpectedArrivalTime']
    new_row['ExpectedDepartureTime'] = row['ExpectedDepartureTime']
    new_row['TripStopStatus'] = row['TripStopStatus']
    new_row['SideCode'] = row['SideCode']
    new_row['NumberOfCoaches'] = row['NumberOfCoaches']
    new_row['WheelChairAccessible'] = row['WheelChairAccessible']
    new_row['TimingPointDataOwnerCode'] = row['TimingPointDataOwnerCode']
    new_row['TimingPointCode'] = row['TimingPointCode']
    new_row['JourneyStopType'] = row['JourneyStopType']
    new_row['VehicleNumber'] = row['VehicleNumber']

    return new_row

def normalize_kv7_lsg(row, counter):
    new_row = {}
    # new_row['id'] = counter
    new_row['DataOwnerCode'] = row['DataOwnerCode']
    new_row['LocalServiceLevelCode'] = row['LocalServiceLevelCode']

    return new_row

def normalize_kv7_lsgv(row, counter):
    new_row = {}
    # new_row['id'] = counter
    new_row['DataOwnerCode'] = row['DataOwnerCode']
    new_row['LocalServiceLevelCode'] = row['LocalServiceLevelCode']
    new_row['OperationDate'] = row['OperationDate']

    return new_row

def normalize_kv7_sa(row, counter):
    new_row = {}
    # new_row['id'] = counter
    new_row['DataOwnerCode'] = row['DataOwnerCode']
    new_row['StopAreaCode'] = row['StopAreaCode']
    # new_row['StopAreaName'] = row['StopAreaName']

    return new_row

def normalize_kv7_do(row, counter):
    new_row = {}
    # new_row['id'] = counter
    new_row['DataOwnerCode'] = row['DataOwnerCode']
    new_row['DataOwnerType'] = row['DataOwnerType']
    new_row['DataOwnerName'] = row['DataOwnerName']
    # new_row['DataOwnerCompanyNumber'] = row['DataOwnerCompanyNumber']

    return new_row

def normalize_kv7_d(row, counter):
    new_row = {}
    # new_row['id'] = counter
    new_row['DataOwnerCode'] = row['DataOwnerCode']
    new_row['DestinationCode'] = row['DestinationCode']
    new_row['DestinationName50'] = row['DestinationName50']
    new_row['DestinationName30'] = row['DestinationName30']
    new_row['DestinationName24'] = row['DestinationName24']
    new_row['DestinationName19'] = row['DestinationName19']
    new_row['DestinationName16'] = row['DestinationName16']
    # new_row['DestinationDetail24'] = row['DestinationDetail24']
    new_row['DestinationDetail19'] = row['DestinationDetail19']
    new_row['DestinationDetail16'] = row['DestinationDetail16']
    new_row['DestinationDisplay16'] = row['DestinationDisplay16']
    # new_row['DestinationName21'] = row['DestinationName21']
    # new_row['DestinationDetail21'] = row['DestinationDetail21']
    # new_row['RelevantDestNameDetail'] = row['RelevantDestNameDetail']
    # new_row['DestIcon'] = row['DestIcon']
    # new_row['DestColor'] = row['DestColor']
    # new_row['DestTextColor'] = row['DestTextColor']

    return new_row

def normalize_kv7_utp(row, counter):
    new_row = {}
    # new_row['id'] = counter
    new_row['DataOwnerCode'] = row['DataOwnerCode']
    new_row['UserStopCode'] = row['UserStopCode']
    new_row['TimingPointDataOwnerCode'] = row['TimingPointDataOwnerCode']
    new_row['TimingPointCode'] = row['TimingPointCode']
    # new_row['GetIn'] = row['GetIn']
    # new_row['GetOut'] = row['GetOut']

    return new_row

def normalize_kv7_l(row, counter):
    new_row = {}
    # new_row['id'] = counter
    new_row['DataOwnerCode'] = row['DataOwnerCode']
    new_row['LinePlanningNumber'] = row['LinePlanningNumber']
    new_row['LinePublicNumber'] = row['LinePublicNumber']
    new_row['LineName'] = row['LineName']
    new_row['LineVeTagNumber'] = row['LineVeTagNumber']
    new_row['TransportType'] = row['TransportType']
    # new_row['LineIcon'] = row['LineIcon']
    # new_row['LineColor'] = row['LineColor']
    # new_row['LineTextColor'] = row['LineTextColor']

    return new_row

def normalize_kv7_lsgpt(row, counter):
    new_row = {}
    # new_row['id'] = counter
    new_row['DataOwnerCode'] = row['DataOwnerCode']
    new_row['LocalServiceLevelCode'] = row['LocalServiceLevelCode']
    new_row['LinePlanningNumber'] = row['LinePlanningNumber']
    new_row['JourneyNumber'] = row['JourneyNumber']
    new_row['FortifyOrderNumber'] = row['FortifyOrderNumber']
    new_row['UserStopCode'] = row['UserStopCode']
    new_row['UserStopOrderNumber'] = row['UserStopOrderNumber']
    new_row['LineDirection'] = row['LineDirection']
    new_row['DestinationCode'] = row['DestinationCode']
    new_row['TargetArrivalTime'] = row['TargetArrivalTime']
    new_row['TargetDepartureTime'] = row['TargetDepartureTime']
    new_row['SideCode'] = row['SideCode']
    new_row['WheelChairAccessible'] = row['WheelChairAccessible']
    new_row['JourneyStopType'] = row['JourneyStopType']
    new_row['IsTimingStop'] = row['IsTimingStop']
    new_row['ProductFormulaType'] = row['ProductFormulaType']
    new_row['JourneyPatternCode'] = row['JourneyPatternCode']
    # new_row['GetIn'] = row['GetIn']
    # new_row['GetOut'] = row['GetOut']
    # new_row['ShowFlexibleTrip'] = row['ShowFlexibleTrip']
    # new_row['LineDestIcon'] = row['LineDestIcon']
    # new_row['LineDestColor'] = row['LineDestColor']
    # new_row['LineDestTextColor'] = row['LineDestTextColor']
    # new_row['BlockCode'] = row['BlockCode']
    # new_row['SequenceInBlock'] = row['SequenceInBlock']
    # new_row['VehicleJourneyType'] = row['VehicleJourneyType']

    return new_row

def normalize_kv7_tp(row, counter):
    new_row = {}
    # new_row['id'] = counter
    new_row['DataOwnerCode'] = row['DataOwnerCode']
    new_row['TimingPointCode'] = row['TimingPointCode']
    new_row['TimingPointName'] = row['TimingPointName']
    new_row['TimingPointTown'] = row['TimingPointTown']
    # new_row['StopAreaCode'] = row['StopAreaCode']
    # new_row['LocationX_EW'] = row['LocationX_EW']
    # new_row['LocationY_NS'] = row['LocationY_NS']
    # new_row['LocationZ'] = row['LocationZ']

    return new_row

def drop_table():
    return """
        DROP TABLE IF EXISTS kv7_dataowner;
        DROP TABLE IF EXISTS kv7_line;
        DROP TABLE IF EXISTS kv7_destination;
        DROP TABLE IF EXISTS kv7_destinationvia;
        DROP TABLE IF EXISTS kv7_timingpoint;
        DROP TABLE IF EXISTS kv7_usertimingpoint;
        DROP TABLE IF EXISTS kv7_localservicegrouppasstime;
        DROP TABLE IF EXISTS kv7_localservicegroup;
        DROP TABLE IF EXISTS kv7_localservicegroupvalidity;
        DROP TABLE IF EXISTS tmp_kv7_dataowner;
        DROP TABLE IF EXISTS tmp_kv7_line;
        DROP TABLE IF EXISTS tmp_kv7_destination;
        DROP TABLE IF EXISTS tmp_kv7_destinationvia;
        DROP TABLE IF EXISTS tmp_kv7_timingpoint;
        DROP TABLE IF EXISTS tmp_kv7_usertimingpoint;
        DROP TABLE IF EXISTS tmp_kv7_localservicegrouppasstime;
        DROP TABLE IF EXISTS tmp_kv7_localservicegroup;
        DROP TABLE IF EXISTS tmp_kv7_localservicegroupvalidity;
    """

def tmp_table():
    return """
        CREATE TABLE "tmp_kv7_dataowner" (
                "dataownercode"          VARCHAR(10)   NOT NULL,
                "dataownertype"          VARCHAR(10)   NOT NULL,
                "dataownername"          VARCHAR(30)   NOT NULL,
                "dataownercompanynumber" DECIMAL(3)
        );
        CREATE TABLE "tmp_kv7_line" (
                "dataownercode"      VARCHAR(10)   NOT NULL,
                "lineplanningnumber" VARCHAR(10)   NOT NULL,
                "linepublicnumber"   VARCHAR(4)    NOT NULL,
                "linename"           VARCHAR(50),
                "linevetagnumber"    DECIMAL(3),
                "transporttype"      VARCHAR(5)    NOT NULL
        );
        CREATE TABLE "tmp_kv7_destination" (
                "dataownercode"        VARCHAR(10)   NOT NULL,
                "destinationcode"      VARCHAR(10)   NOT NULL,
                "destinationname50"    VARCHAR(50)   NOT NULL,
                "destinationname30"    VARCHAR(30),
                "destinationname24"    VARCHAR(24),
                "destinationname19"    VARCHAR(19),
                "destinationname16"    VARCHAR(16)   NOT NULL,
                "destinationdetail24"  VARCHAR(24),
                "destinationdetail19"  VARCHAR(19),
                "destinationdetail16"  VARCHAR(16),
                "destinationdisplay16" VARCHAR(16)
        );
        CREATE TABLE "tmp_kv7_destinationvia" (
                "dataownercode"         VARCHAR(10)   NOT NULL,
                "destinationcodep"      VARCHAR(10)   NOT NULL,
                "destinationcodec"      VARCHAR(10)   NOT NULL,
                "destinationviaordernr" INT       NOT NULL
        );
        CREATE TABLE "tmp_kv7_timingpoint" (
                "dataownercode"   VARCHAR(10)   NOT NULL,
                "timingpointcode" VARCHAR(10)   NOT NULL,
                "timingpointname" VARCHAR(50)   NOT NULL,
                "timingpointtown" VARCHAR(50)   NOT NULL,
                "stopareacode"    VARCHAR(10)
        );
        CREATE TABLE "tmp_kv7_usertimingpoint" (
                "dataownercode"            VARCHAR(10)   NOT NULL,
                "userstopcode"             VARCHAR(10)   NOT NULL,
                "timingpointdataownercode" VARCHAR(10)   NOT NULL,
                "timingpointcode"          VARCHAR(10)   NOT NULL
        );
        CREATE TABLE "tmp_kv7_localservicegrouppasstime" (
                "dataownercode"         VARCHAR(10)   NOT NULL,
                "localservicelevelcode" VARCHAR(10)   NOT NULL,
                "lineplanningnumber"    VARCHAR(10)   NOT NULL,
                "journeynumber"         DECIMAL(6)    NOT NULL,
                "fortifyordernumber"    DECIMAL(2)    NOT NULL,
                "userstopcode"          VARCHAR(10)   NOT NULL,
                "userstopordernumber"   DECIMAL(3)    NOT NULL,
                "linedirection"         DECIMAL       NOT NULL,
                "destinationcode"       VARCHAR(10)   NOT NULL,
                "targetarrivaltime"     VARCHAR(8)    NOT NULL,
                "targetdeparturetime"   VARCHAR(8)    NOT NULL,
                "sidecode"              VARCHAR(10)   NOT NULL,
                "wheelchairaccessible"  VARCHAR(15),
                "journeystoptype"       VARCHAR(12)   NOT NULL,
                "istimingstop"          BOOLEAN       NOT NULL,
                "productformulatype"    DECIMAL(4)
        );
        CREATE TABLE "tmp_kv7_localservicegroup" (
                "dataownercode"         VARCHAR(10)   NOT NULL,
                "localservicelevelcode" VARCHAR(10)   NOT NULL
        );
        CREATE TABLE "tmp_kv7_localservicegroupvalidity" (
                "dataownercode"         VARCHAR(10)   NOT NULL,
                "localservicelevelcode" VARCHAR(10)   NOT NULL,
                "operationdate"         DATE          NOT NULL
        );
    """

def main_table():
    return """
        CREATE TABLE "kv7_dataowner" (
                "dataownercode"          VARCHAR(10)   NOT NULL,
                "dataownertype"          VARCHAR(10)   NOT NULL,
                "dataownername"          VARCHAR(30)   NOT NULL,
                "dataownercompanynumber" DECIMAL(3),
                CONSTRAINT "dataowner_dataownercode_pkey" PRIMARY KEY ("dataownercode")
        );
        CREATE TABLE "kv7_line" (
                "dataownercode"      VARCHAR(10)   NOT NULL,
                "lineplanningnumber" VARCHAR(10)   NOT NULL,
                "linepublicnumber"   VARCHAR(4)    NOT NULL,
                "linename"           VARCHAR(50),
                "linevetagnumber"    DECIMAL(3),
                "transporttype"      VARCHAR(5)    NOT NULL,
                CONSTRAINT "line_dataownercode_lineplanningnumber_pkey" PRIMARY KEY ("dataownercode", "lineplanningnumber")
        );
        CREATE TABLE "kv7_destination" (
                "dataownercode"        VARCHAR(10)   NOT NULL,
                "destinationcode"      VARCHAR(10)   NOT NULL,
                "destinationname50"    VARCHAR(50)   NOT NULL,
                "destinationname30"    VARCHAR(30),
                "destinationname24"    VARCHAR(24),
                "destinationname19"    VARCHAR(19),
                "destinationname16"    VARCHAR(16)   NOT NULL,
                "destinationdetail24"  VARCHAR(24),
                "destinationdetail19"  VARCHAR(19),
                "destinationdetail16"  VARCHAR(16),
                "destinationdisplay16" VARCHAR(16),
                CONSTRAINT "destination_dataownercode_destinationcode_pkey" PRIMARY KEY ("dataownercode", "destinationcode")
        );
        CREATE TABLE "kv7_destinationvia" (
                "dataownercode"         VARCHAR(10)   NOT NULL,
                "destinationcodep"      VARCHAR(10)   NOT NULL,
                "destinationcodec"      VARCHAR(10)   NOT NULL,
                "destinationviaordernr" INT       NOT NULL,
                CONSTRAINT "destinationvia_dataownercode_destinationcodep_destinationcodec_pkey" PRIMARY KEY ("dataownercode", "destinationcodep", "destinationcodec")
        );
        CREATE TABLE "kv7_timingpoint" (
                "dataownercode"   VARCHAR(10)   NOT NULL,
                "timingpointcode" VARCHAR(10)   NOT NULL,
                "timingpointname" VARCHAR(50)   NOT NULL,
                "timingpointtown" VARCHAR(50)   NOT NULL,
                "stopareacode"    VARCHAR(10),
                CONSTRAINT "timingpoint_dataownercode_timingpointcode_pkey" PRIMARY KEY ("dataownercode", "timingpointcode")
        );
        CREATE TABLE "kv7_usertimingpoint" (
                "dataownercode"            VARCHAR(10)   NOT NULL,
                "userstopcode"             VARCHAR(10)   NOT NULL,
                "timingpointdataownercode" VARCHAR(10)   NOT NULL,
                "timingpointcode"          VARCHAR(10)   NOT NULL,
                CONSTRAINT "usertimingpoint_dataownercode_userstopcode_pkey" PRIMARY KEY ("dataownercode", "userstopcode")
        );
        CREATE TABLE "kv7_localservicegrouppasstime" (
                "dataownercode"         VARCHAR(10)   NOT NULL,
                "localservicelevelcode" VARCHAR(10)   NOT NULL,
                "lineplanningnumber"    VARCHAR(10)   NOT NULL,
                "journeynumber"         DECIMAL(6)    NOT NULL,
                "fortifyordernumber"    DECIMAL(2)    NOT NULL,
                "userstopcode"          VARCHAR(10)   NOT NULL,
                "userstopordernumber"   DECIMAL(3)    NOT NULL,
                "linedirection"         DECIMAL       NOT NULL,
                "destinationcode"       VARCHAR(10)   NOT NULL,
                "targetarrivaltime"     VARCHAR(8)    NOT NULL,
                "targetdeparturetime"   VARCHAR(8)    NOT NULL,
                "sidecode"              VARCHAR(10)   NOT NULL,
                "wheelchairaccesible"   VARCHAR(15),
                "journeystoptype"       VARCHAR(12)   NOT NULL,
                "istimingstop"          BOOLEAN       NOT NULL,
                "productformulatype"    DECIMAL(4),
                CONSTRAINT "localservicegrouppasstime_dataownercode_localservicelevelcode_lineplanningnumber_journeynumber_fortifyordernumber_userstopcode_userstopordernumber_pkey" PRIMARY KEY ("dataownercode", "localservicelevelcode", "lineplanningnumber", "journeynumber", "fortifyordernumber", "userstopcode", "userstopordernumber")
        );
        CREATE TABLE "kv7_localservicegroup" (
                "dataownercode"         VARCHAR(10)   NOT NULL,
                "localservicelevelcode" VARCHAR(10)   NOT NULL,
                CONSTRAINT "localservicegroup_dataownercode_localservicelevelcode_pkey" PRIMARY KEY ("dataownercode", "localservicelevelcode")
        );
        CREATE TABLE "kv7_localservicegroupvalidity" (
                "dataownercode"         VARCHAR(10)   NOT NULL,
                "localservicelevelcode" VARCHAR(10)   NOT NULL,
                "operationdate"         DATE          NOT NULL,
                CONSTRAINT "localservicegroupvalidity_dataownercode_localservicelevelcode_operationdate_pkey" PRIMARY KEY ("dataownercode", "localservicelevelcode", "operationdate")
        );
        GRANT SELECT ON kv7_dataowner TO postgres;
        GRANT SELECT ON kv7_line TO postgres;
        GRANT SELECT ON kv7_destination TO postgres;
        GRANT SELECT ON kv7_destinationvia TO postgres;
        GRANT SELECT ON kv7_timingpoint TO postgres;
        GRANT SELECT ON kv7_usertimingpoint TO postgres;
        GRANT SELECT ON kv7_localservicegrouppasstime TO postgres;
        GRANT SELECT ON kv7_localservicegroup TO postgres;
        GRANT SELECT ON kv7_localservicegroupvalidity TO postgres;
    """

def type_data(table):
    if table == "kv7_line":
        return '%s,%s,%s,%s,%s,%s'
    elif table == "kv7_destination":
        return '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'
    elif table == "kv7_destinationvia":
        return '%s,%s,%s,%s'
    elif table == "kv7_timingpoint":
        return '%s,%s,%s,%s,%s'
    elif table == "kv7_usertimingpoint":
        return '%s,%s,%s,%s'
    elif table == "kv7_localservicegrouppasstime":
        return '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'
    elif table == "kv7_localservicegroup":
        return '%s,%s'
    elif table == "kv7_localservicegroupvalidity":
        return '%s,%s,%s'
