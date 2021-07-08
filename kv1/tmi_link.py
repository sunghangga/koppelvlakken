class tmi_link():
    def __init__(self):
        self.data = []
        self.types = [
            {'name': 'DataOwnerCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'UserStopCodeBegin', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'UserStopCodeEnd', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'ValidFrom', 'aard': 'o', 'type': 'D', 'length': 10 },
            {'name': 'Distance', 'aard': '+', 'type': 'N', 'length': 6 },
            {'name': 'Description', 'aard': 'o', 'type': 'A', 'length': 255 },
            {'name': 'TransportType', 'aard': '#', 'type': 'A', 'length': 5 },
            # {'name': 'TransportType', 'aard': 'o', 'type': 'A', 'length': 5 },
            ]
        self.references = None

    def parse(self, version, implicit, data_owner_code, elements):
        user_stop_code_begin, user_stop_code_end, valid_from, distance, description, transport_type = elements
        self.data.append([version, implicit, data_owner_code, user_stop_code_begin, user_stop_code_end, valid_from, distance, description, transport_type])
