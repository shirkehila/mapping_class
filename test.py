from anytree import Node, RenderTree
from field_node import FieldNode

udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)

my_field = ElasticsearchFieldNode("is_ugly", "boolean", [])

for pre, fill, node in RenderTree(my_field):
    print("%s%s" % (pre, node.name))
