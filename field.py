from field_definition import FieldDefinition
from typing import Set

SECONDARY_FIELD_DEFINITION_KEY = "fields"


class Field:
    def get_data_types(self) -> Set[str]:
        data_types = {self.main_definition.data_type}
        secondary_data_types = [field_definition.data_type for field_definition in self.secondary_definitions]
        data_types = data_types.union(set(secondary_data_types))
        return data_types

    def __init__(self, field_name, field_json: dict):
        self.secondary_definitions = []
        if SECONDARY_FIELD_DEFINITION_KEY in field_json:
            secondary_fields = field_json[SECONDARY_FIELD_DEFINITION_KEY]
            del field_json[SECONDARY_FIELD_DEFINITION_KEY]
            for secondary_field_name, json_field_definition in secondary_fields.items():
                self.secondary_definitions.append(FieldDefinition(field_name, json_field_definition))
        self.main_definition = FieldDefinition(field_name, field_json)


if __name__ == '__main__':
    my_field = Field("my_field", {
        "type": "geo_point",
        "fields": {
            "my_field_nested": {
                "type": "text",
                "analyzer": "simple"
            },
            "keyword": {
                "type": "keyword"
            }
        }
    })

    print(my_field.get_data_types())
