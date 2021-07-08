class tmi_notice():
    def __init__(self):
        self.data = []
        self.types = [
            {'name': 'DataOwnerCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'NoticeCode', 'aard': '#', 'type': 'A', 'length': 20 },
            {'name': 'NoticeContent', 'aard': '+', 'type': 'A', 'length': 1024 },
            ]
        self.references = None

    def parse(self, version, implicit, data_owner_code, elements):
        notice_code, notice_content = elements
        self.data.append([version, implicit, data_owner_code, notice_code, notice_content])
