from field_node import FieldNode
from anytree import RenderTree, PostOrderIter


class Mapping:
    @staticmethod
    def get_field_type(field_definition):
        if "type" not in field_definition:
            return "object"
        return field_definition["type"]

    def get_data_types_in_mapping(self):
        return set.union(*[field.get_data_types() for field in PostOrderIter(self.fields)]).difference({"root_object"})

    def get_number_of_fields(self):
        return len(self.fields.leaves)

    def init_fields(self, json_mapping_definition, parent_field):
        for field_name, field_definition in json_mapping_definition["properties"].items():
            if field_name == "my_field":
                print()
            field_type = self.get_field_type(field_definition)
            if field_type not in ["nested", "object"]:
                FieldNode(field_name, field_definition, parent=parent_field)
            else:
                new_parent = FieldNode(field_name, {"type": field_type}, parent=parent_field)
                self.init_fields(field_definition, new_parent)

    def __init__(self, json_mapping_definition):
        self.fields = FieldNode("mapping", {
            "type": "root_object"
        })
        self.init_fields(json_mapping_definition, self.fields)


mapping_definition_example = {
    "properties": {
        "region": {
            "type": "keyword"
        },
        "manager": {
            "properties": {
                "age": {"type": "integer"},
                "name": {
                    "properties": {
                        "first": {"type": "text"},
                        "last": {"type": "text"}
                    }
                }
            }
        },
        "my_field": {
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
        }
    }
}

my_mappings = Mapping(mapping_definition_example)
fields = my_mappings.fields
for pre, _, node in RenderTree(fields):
    details = f"{node.main_definition.field_name} ({node.main_definition.data_type})"
    treestr = u"%s%s" % (pre, details)
    print(treestr.ljust(8))
print(f"The mappings depth is {fields.height}")
print(f"field types: {', '.join(my_mappings.get_data_types_in_mapping())}")
print(f"number of fields: {my_mappings.get_number_of_fields()}")
