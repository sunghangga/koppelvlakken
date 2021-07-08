from helper import day2int

class tmi_ntcassgnm():
    def __init__(self):
        self.data = []
        self.types = [
            {'name': 'DataOwnerCode', 'aard': '+', 'type': 'A', 'length': 10 },
            {'name': 'NoticeCode', 'aard': '+', 'type': 'A', 'length': 20 },
            {'name': 'AssignedObject', 'aard': '+', 'type': 'A', 'length': 8 },
            {'name': 'TimetableVersionCode', 'aard': 'o', 'type': 'A', 'length': 10 },
            {'name': 'OrganizationalUnitCode', 'aard': 'o', 'type': 'A', 'length': 10 },
            {'name': 'ScheduleCode', 'aard': 'o', 'type': 'A', 'length': 10 },
            {'name': 'ScheduleTypeCode', 'aard': 'o', 'type': 'A', 'length': 10 },
            {'name': 'PeriodGroupCode', 'aard': 'o', 'type': 'A', 'length': 10 },
            {'name': 'SpecificDayCode', 'aard': 'o', 'type': 'A', 'length': 10 },
            {'name': 'DayType', 'aard': 'o', 'type': 'S' },
            {'name': 'LinePlanningNumber', 'aard': '+', 'type': 'A', 'length': 10 },
            {'name': 'JourneyNumber', 'aard': 'o', 'type': 'N', 'length': 6 },
            {'name': 'StopOrder', 'aard': 'o', 'type': 'N', 'length': 4 },
            {'name': 'JourneyPatternCode', 'aard': 'o', 'type': 'A', 'length': 10 },
            {'name': 'TimingLinkOrder', 'aard': 'o', 'type': 'N', 'length': 3 },
            {'name': 'UserStopCode', 'aard': 'o', 'type': 'A', 'length': 10 },
            ]
        self.references = {'pujo': ['TimetableVersionCode', 'OrganizationalUnitCode', 'PeriodGroupCode', 'SpecificDayCode', 'DayType', 'LinePlanningNumber', 'JourneyNumber'],
                           'pujopass': ['OrganizationalUnitCode', 'ScheduleCode', 'ScheduleTypeCode', 'LinePlanningNumber', 'JourneyNumber', 'StopOrder'],
                           'line': ['LinePlanningNumber'],
                           'jopatili': ['LinePlanningNumber', 'JourneyPatternCode', 'TimingLinkOrder']
                           }

    def parse(self, version, implicit, data_owner_code, elements):
        notice_code, assigned_object, timetable_version_code, organizational_unit_code, schedule_code, schedule_type_code, period_group_code, specific_day_code, day_type, line_planning_number, journey_number, stop_order, journey_pattern_code, timing_link_order, user_stop_code = elements
        day_type = str(day2int(day_type))
        self.data.append([version, implicit, data_owner_code, notice_code, assigned_object, timetable_version_code, organizational_unit_code, schedule_code, schedule_type_code, period_group_code, specific_day_code, day_type, line_planning_number, journey_number, stop_order, journey_pattern_code, timing_link_order, user_stop_code])
