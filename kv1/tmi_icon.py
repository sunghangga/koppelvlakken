class tmi_icon():
    def __init__(self):
        self.data = []
        self.types = [
            {'name': 'DataOwnerCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'IconNumber', 'aard': '#', 'type': 'N', 'length': 4 },
            {'name': 'IconURI', 'aard': 'o', 'type': 'A', 'length': 1024 },
            ]
        self.references = None

    def parse(self, version, implicit, data_owner_code, elements):
        icon_number, icon_uri = elements
        self.data.append([version, implicit, data_owner_code, icon_number, icon_uri])
