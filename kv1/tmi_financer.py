class tmi_financer():
    def __init__(self):
        self.data = []
        self.types = [
            {'name': 'DataOwnerCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'FinancerCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'Description', 'aard': '+', 'type': 'A', 'length': 255 },
            ]
        self.references = None

    def parse(self, version, implicit, data_owner_code, elements):
        financer_code, description = elements
        self.data.append([version, implicit, data_owner_code, financer_code, description])
