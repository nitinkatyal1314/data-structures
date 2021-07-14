from .traversal import TreeWalkStrategy, WalkAPI
from .base import TreeNode


class TreeAPI(object):
    """
    Tree implementation with in-order default walk strategy.
    """

    # Default walk strategy for tree
    DEFAULT_WALK_STRATEGY = TreeWalkStrategy.DEPTH_FIRST

    def __init__(self):
        """
        Initializes the root node and the traversal API.
        """
        self.traversal_api = WalkAPI(strategy=self.DEFAULT_WALK_STRATEGY)

    def _add_children_to_node(self, node, children_data: list):
        """
        Creates the tree based on the data dictionary. Tree assumes mapping of tree
        in a dictionary, and creates nodes with Depth-First strategy using recursion.
        :param node:  a tree node instance
        :type node: TreeNode
        :param children_data:
        :type children_data:
        :return:
        :rtype:
        """
        if len(children_data) > 0:
            for child_data in children_data:
                # raise exception and if node data is not valid
                try:
                    TreeNode.validate_node(child_data)
                except Exception as e:
                    raise e

                child_node = TreeNode(name=child_data[TreeNode.NAME],
                                      data=child_data[TreeNode.DATA])

                node.add_child(child_node)
                self._add_children_to_node(child_node, child_data[TreeNode.CHILDREN])

    def parse(self, tree_data: dict):
        """
        Will parse tree data into the tree and return the root node.
        :param tree_data: data used to load tree.
        :type tree_data: dict
        :return:
        :rtype:
        """

        # raise exception if node data is not valid
        try:
            TreeNode.validate_node(tree_data)
        except Exception as e:
            raise e

        root = TreeNode(name=tree_data[TreeNode.NAME], data=tree_data[TreeNode.DATA])
        self._add_children_to_node(root, tree_data[TreeNode.CHILDREN])
        return root

    def walk(self, root: TreeNode, strategy: str = TreeWalkStrategy.DEPTH_FIRST, callback=None, *args, **kwargs):
        """
        Walks the tree with a strategy. Need Callback function to process node during walk.
        :param root: root node of the tree
        :type root: TreeNode
        :param strategy: strategy to use when traversing (DFS/ BFS)
        :type strategy: str
        :param callback: The callback function executed when node is visited during traversal
        :type callback: function
        :param args: arguments for callback function
        :type args:
        :param kwargs: keyword arguments for callback function
        :type kwargs:
        :return:
        :rtype:
        """

        self.traversal_api = WalkAPI(strategy=strategy)
        self.traversal_api.start_traversal(root, callback, *args, **kwargs)

    def as_dict(self, root: TreeNode):
        """
        Converts tree to dict given its root node.

        :param root: The root node of the tree.
        :type root: TreeNode
        :return:
        :rtype:
        """
        tree_as_dict = {TreeNode.NAME: root.name, TreeNode.DATA: root.data, TreeNode.CHILDREN: []}
        self.traversal_api.traverse_dfs_tree_to_dict(root, tree_as_dict[TreeNode.CHILDREN])

        return tree_as_dict

    def has_node(self, root_node: TreeNode, node_name: str):
        """
        Check if the node with name exist in the tree given it's root node
        :param root_node: root node of the tree
        :type root_node: TreeNode
        :param node_name: name of the node to search
        :type node_name: str
        :return: True/ False if the node is found / not-found
        :rtype: bool
        """
        return self.traversal_api.search(root_node, node_name)

    def get_height(self, root_node: TreeNode):
        """
        Get the height of the tree given the root node.

        :param root_node: root node of the tree
        :type root_node: TreeNode
        :return: height of the tree
        :rtype: int
        """

        return self.traversal_api.traverse_get_height(root_node)









