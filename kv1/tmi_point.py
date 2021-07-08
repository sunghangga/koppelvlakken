class tmi_point():
    def __init__(self):
        self.data = []
        self.types = [
            {'name': 'DataOwnerCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'PointCode', 'aard': '#', 'type': 'A', 'length': 10 },
            {'name': 'ValidFrom', 'aard': 'o', 'type': 'D', 'length': 10 },
            {'name': 'PointType', 'aard': '+', 'type': 'A', 'length': 10 },
            {'name': 'CoordinateSystemType', 'aard': '+', 'type': 'A', 'length': 10 },
            {'name': 'LocationX_EW', 'aard': '+', 'type': 'A', 'length': 15 },
            {'name': 'LocationY_NS', 'aard': '+', 'type': 'A', 'length': 15 },
            {'name': 'LocationZ', 'aard': 'o', 'type': 'A', 'length': 15 },
            {'name': 'Description', 'aard': 'o', 'type': 'A', 'length': 255 },
            ]
        self.references = None

    def parse(self, version, implicit, data_owner_code, elements):
        point_code, valid_from, point_type, coordinate_system_type, location_x_ew, location_y_ns, location_z, description = elements
        self.data.append([version, implicit, data_owner_code, point_code, valid_from, point_type, coordinate_system_type, location_x_ew, location_y_ns, location_z, description])
