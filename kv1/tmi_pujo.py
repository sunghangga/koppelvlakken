from helper import time32, wheelchair, boolsql, daytype2bitstring, day2int, timeform

class tmi_pujo():
    def __init__(self):
        self.data = []
        self.types = [
            {'name': 'DataOwnerCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'TimetableVersionCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'OrganizationalUnitCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'PeriodGroupCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'SpecificDayCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'DayType', 'aard': '#', 'type': 'S' },
            {'name': 'LinePlanningNumber', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'JourneyNumber', 'aard': '#', 'type': 'N', 'length': 6 },
            {'name': 'TimeDemandGroupCode', 'aard': '+', 'type': 'A', 'length': 10 },
            {'name': 'JourneyPatternCode', 'aard': '+', 'type': 'A', 'length': 10 },
            {'name': 'DepartureTime', 'aard': '+', 'type': 'T', 'length': 8 },
            {'name': 'WheelChairAccessible', 'aard': '+', 'type': 'B', 'length': 5 },
            {'name': 'DataOwnerIsOperator', 'aard': '+', 'type': 'B', 'length': 5 },
            {'name': 'PlannedMonitored', 'aard': '+', 'type': 'B', 'length': 5 },
            {'name': 'ProductFormulaType', 'aard': 'o', 'type': 'N', 'length': 4 },
            {'name': 'ShowFlexibleTrip', 'aard': 'o', 'type': 'A', 'length': 8 },
        ]
        self.references = {'tive': ['OrganizationalUnitCode', 'TimetableVersionCode', 'PeriodGroupCode', 'SpecificDayCode'],
                           'timdemgrp': ['LinePlanningNumber', 'JourneyPatternCode', 'TimeDemandGroupCode']}

    def parse(self, version, implicit, data_owner_code, elements):
        timetable_version_code, organizational_unit_code, period_group_rode, specific_day_code, day_type, line_planning_number, journey_number, time_demand_group_code, journey_pattern_code, departure_time, wheel_chair_accessible, data_owner_is_operator, planned_monitored, product_formula_type, show_flexible_trip = elements
        
        wheel_chair_accessible = wheelchair(wheel_chair_accessible)
        departure_time = timeform(departure_time)
        day_type = str(day2int(day_type))

        self.data.append([version, implicit, data_owner_code, timetable_version_code, organizational_unit_code, period_group_rode, specific_day_code,
                          day_type, line_planning_number, journey_number, time_demand_group_code, journey_pattern_code,
                          departure_time, wheel_chair_accessible, data_owner_is_operator, planned_monitored, product_formula_type, show_flexible_trip])
