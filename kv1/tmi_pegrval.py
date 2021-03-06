class tmi_pegrval():
    def __init__(self):
        self.data = []
        self.types = [
            {'name': 'DataOwnerCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'OrganizationalUnitCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'PeriodGroupCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'ValidFrom', 'aard': '#', 'type': 'D', 'length': 10 },
            {'name': 'ValidThru', 'aard': '+', 'type': 'D', 'length': 10 },
            ]
        # self.references = {'orun': ['OrganizationalUnitCode'] }
        self.references = {'orun': ['OrganizationalUnitCode'],
                          'pegr': ['PeriodGroupCode']}

    def parse(self, version, implicit, data_owner_code, elements):
        organizational_unit_code, period_group_code, valid_from, valid_thru = elements
        self.data.append([version, implicit, data_owner_code, organizational_unit_code, period_group_code, valid_from, valid_thru])
