from typing import Mapping, Any


class FieldDefinition:
    field_name: str
    data_type: str
    settings: Mapping[str, Any]

    def __init__(self, field_name, json_field_definition):
        self.field_name = field_name
        self.data_type = json_field_definition["type"]
        del json_field_definition["type"]
        self.settings = json_field_definition
