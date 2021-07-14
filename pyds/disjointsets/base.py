from pyds.tree import TreeAPI, TreeNodeKeys
from .exceptions import NodeNotFoundInSet


class DisjointSets(object):
    """
    Implement disjoint sets using a tree.
    """

    # keys for creating tree dict
    name = TreeNodeKeys.NAME
    data = TreeNodeKeys.DATA
    children = TreeNodeKeys.CHILDREN

    def __init__(self, nodes: list):
        """
        Initializes a list containing TreeNodes. As union operation is performed over these
        nodes they will merge together. If two nodes have the same root node
        they will form a disjoint set.

        """

        self.all_sets = []
        self.tree_api = TreeAPI()
        for node_name in nodes:

            if node_name not in list(map(lambda node: node.name, self.all_sets)):
                tree_data = {
                    self.name: node_name,
                    self.children: [],
                    self.data: {}
                }

                tree_root = self.tree_api.parse(tree_data)
                self.all_sets.append(tree_root)
            else:
                print("Key %s already present. Skipping this node." % node_name)

    def is_disjoint(self, node1, node2):
        """
        Checks if the two nodes are disjoint (have the same root node).

        :param node1:
        :type node1:
        :param node2:
        :type node2:
        :return:
        :rtype:
        """
        root_node1 = self.find_root(node1)
        root_node2 = self.find_root(node2)

        if root_node1 == root_node2:
            return False
        else:
            return True

    def union(self, node1, node2):
        """
        Take union of node1 and node2. Combines the tree in the self.all_sets
        containing node1 and node2. The tree with smaller height is added at the
        right child, and its stand-alone set is removed all_sets.

        :param node1: name of the first node
        :type node1: str
        :param node2: name of the second node
        :type node2: str
        :return:
        :rtype:
        """

        tree_node_1 = None
        tree_node_2 = None

        for tree in self.all_sets:
            status_node1 = self.tree_api.has_node(tree, node1)
            status_node2 = self.tree_api.has_node(tree, node2)
            if status_node1:
                tree_node_1 = tree

            if status_node2:
                tree_node_2 = tree

        if tree_node_1 is None:
            raise NodeNotFoundInSet(node1)

        if tree_node_2 is None:
            raise NodeNotFoundInSet(node2)

        if self.tree_api.get_height(tree_node_1) > self.tree_api.get_height(tree_node_2):
            tree_node_1.add_child(tree_node_2)
            self.all_sets.pop(self.all_sets.index(tree_node_2))
        else:
            tree_node_2.add_child(tree_node_1)
            self.all_sets.pop(self.all_sets.index(tree_node_1))

    def find_root(self, node_name):
        """
        Gets the root node name for the input node.

        :param node_name: name of the input node
        :type node_name: str
        :return: name of the root node
        :rtype: str
        """
        root_node_name = None
        for tree in self.all_sets:
            # search node in the tree
            status = self.tree_api.has_node(tree, node_name)
            if status:
                root_node_name = tree.name
                break

        if root_node_name is None:
            raise NodeNotFoundInSet(node_name)

        return root_node_name










