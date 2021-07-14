import json


class TreeNodeKeys(object):
    """
    Holds the key names for the Tree node.
    A Tree class should inherit this to implement node keys.
    """

    NAME = "name"
    DATA = "data"
    CHILDREN = "children"


class TreeNode(TreeNodeKeys):
    """
    Node class for tree data structure. A single node would also be a tree.
    """

    def __init__(self, name: str, data: dict = None):
        """

        :param name: Name for the node
        :type name: str
        :param data: data of the node, a dict
        :type data: dict
        """
        self.name = name
        self.data = data if data is not None else {}

        # children of the node
        self.children = []

    @classmethod
    def validate_node(cls, node: dict):
        """
        Validates that node data has the desirable schema.
        :param node:
        :type node:
        :return:
        :rtype:
        """
        if cls.NAME not in node:
            raise Exception("Could not parse data for node. Missing attribute [%s] ." % cls.NAME)

        if cls.DATA not in node:
            raise Exception("Could not parse data for node %s. Missing attribute [%s] ."
                            % (cls.NAME, cls.DATA))

        if cls.CHILDREN not in node:
            raise Exception("Could not parse data for node %s. Missing attribute [%s] ."
                            % (cls.NAME, cls.CHILDREN))

        return True

    def has_children(self):
        """
        Checks if node has children
        :return: True / False
        :rtype: bool
        """

        if len(self.children) > 0:
            return True
        else:
            return False

    def add_child(self, node):
        """
        Add a node as children.
        :param node:
        :type node:
        :return:
        :rtype:
        """
        self.children.append(node)

    def add_children_at_index(self, index, node):
        """
        Add node to parent at index.
        :param index:
        :type index:
        :param node:
        :type node:
        :return:
        :rtype:
        """
        self.children.insert(index, node)

    def _node_to_dict(self):
        """
        Converts node data to dict
        :return:
        :rtype:
        """

        node_info = {
            self.NAME: self.name,
            self.DATA: self.data
        }

        return node_info

    def serialize(self):
        """
        Serialize node.
        :return:
        :rtype:
        """
        node_as_dict = self._node_to_dict()
        serialized_node = json.dumps(node_as_dict, indent=4)
        return serialized_node

