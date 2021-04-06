from base.tree import TreeNode
from .strategy import TreeWalkStrategy
from .exceptions import InvalidWalkStrategy


class Tree(object):
    """
    Tree implementation with in-order default walk strategy.
    """

    # Default walk strategy for tree
    DEFAULT_WALK_STRATEGY = TreeWalkStrategy.IN_ORDER

    def __init__(self):
        """
        Initialize root Node with empty left and right children
        """
        self.walk_strategy = self.DEFAULT_WALK_STRATEGY
        self.root = None

    def _create_tree(self, node: TreeNode, children_data: list):
        """
        Creates the tree based on the data dictionary. Tree assumes mapping of tree
        in a dictionary, and creates nodes with Depth-First strategy using recursion.
        :param node:
        :type node:
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
                self._create_tree(child_node, child_data[TreeNode.CHILDREN])

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
        self.root = root
        self._create_tree(self.root, tree_data[TreeNode.CHILDREN])
        return self.root

    def _walk(self, node: TreeNode, callback):
        """
        TODO: Add strategy support
        Walk the tree based on the DFS Strategy
        :param callback: callback method to run during traversal
        :type callback:
        :return:
        :rtype:
        """
        # execute callback with node
        callback(node)

        # recurse for child
        for child in node.children:
            self._walk(child, callback)

    def walk(self, callback, strategy: str = None):
        """
        Walks the tree with a strategy. Need Callback function to process node during walk.
        :param callback:
        :type callback:
        :param strategy:
        :type strategy:
        :return:
        :rtype:
        """

        valid_strategies = TreeWalkStrategy.get_valid_strategies()

        if strategy is not None:
            if strategy not in valid_strategies:
                raise InvalidWalkStrategy(valid_strategies)
            else:
                self.walk_strategy = strategy

        if self.root is None:
            raise Exception("No root node to walk.")
        else:
            self._walk(self.root, callback)





