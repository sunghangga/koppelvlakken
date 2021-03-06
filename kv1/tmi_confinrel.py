class tmi_confinrel():
    def __init__(self):
        self.data = []
        self.types = [
            {'name': 'DataOwnerCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'ConFinRelCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'ConcessionAreaCode', 'aard': '+', 'type': 'A', 'length': 10 },
            {'name': 'FinancerCode', 'aard': 'o', 'type': 'A', 'length': 10 },
            ]
        self.references = {'financer': ['FinancerCode'],
                           'conarea': ['ConcessionAreaCode']}
        # self.references = {'conarea': ['ConcessionAreaCode']}

    def parse(self, version, implicit, data_owner_code, elements):
        con_fin_rel_code, concession_area_code, financer_code = elements
        self.data.append([version, implicit, data_owner_code, con_fin_rel_code, concession_area_code, financer_code])
