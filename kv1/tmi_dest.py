class tmi_dest():
    def __init__(self):
        self.data = []
        self.types = [
            {'name': 'DataOwnerCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'DestCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'DestNameFull', 'aard': '+', 'type': 'A', 'length': 50 },
            {'name': 'DestNameMain', 'aard': '+', 'type': 'A', 'length': 24 },
            {'name': 'DestNameDetail', 'aard': 'o', 'type': 'A', 'length': 24 },
            {'name': 'RelevantDestNameDetail', 'aard': '+', 'type': 'B', 'length': 5 },
            {'name': 'DestNameMain21', 'aard': '+', 'type': 'A', 'length': 24 },
            {'name': 'DestNameDetail21', 'aard': 'o', 'type': 'A', 'length': 24 },
            {'name': 'DestNameMain19', 'aard': '+', 'type': 'A', 'length': 24 },
            {'name': 'DestNameDetail19', 'aard': 'o', 'type': 'A', 'length': 24 },
            {'name': 'DestNameMain16', 'aard': '+', 'type': 'A', 'length': 24 },
            {'name': 'DestNameDetail16', 'aard': 'o', 'type': 'A', 'length': 24 },
            {'name': 'DestIcon', 'aard': 'o', 'type': 'N', 'length': 4 },
            {'name': 'DestColor', 'aard': 'o', 'type': 'A', 'length': 6 },
            ]
        # self.references = {'icon': ('DestIcon', 'IconNumber')}
        self.references = None

    def parse(self, version, implicit, data_owner_code, elements):
        dest_code, dest_name_full, dest_name_mail, dest_name_detail, relevant_dest_name_detail, dest_name_main21, dest_name_detail21, dest_name_main19, dest_name_detail19, dest_name_main16, dest_name_detail16, dest_icon, dest_color = elements
        self.data.append([version, implicit, data_owner_code, dest_code, dest_name_full, dest_name_mail, dest_name_detail, relevant_dest_name_detail, dest_name_main21, dest_name_detail21, dest_name_main19, dest_name_detail19, dest_name_main16, dest_name_detail16, dest_icon, dest_color])
