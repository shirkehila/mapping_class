from field import Field
from anytree import NodeMixin


class FieldNode(Field, NodeMixin):  # Add Node feature
    def __init__(self, field_name, json_field_definition, parent=None, children=None):
        super(FieldNode, self).__init__(field_name, json_field_definition)
        self.parent = parent
        if children:
            self.children = children


if __name__ == '__main__':
    my_field = FieldNode("my_field", {
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

