from anytree import Node, RenderTree
from anytree.exporter import DotExporter

class Tree(object):

    def __init__(self,node: str):
        self.parents = []
        node = Node(node)
        self.parents.append(node)

    def add_child(self, parent_index, child):
        node = Node(child, parent=self.parents[parent_index])
        self.parents.append(node)

    def give_me_the_parent(self):
        return self.parents

    def draw(self):
        DotExporter(self.parents[0]).to_picture("ID3-Gini.png")

    def print_tree(self):
        for pre, fill, node in RenderTree(self.parents[0]):
            print("%s%s" % (pre, node.name))

