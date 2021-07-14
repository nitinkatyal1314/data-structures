from .exceptions import InvalidWalkStrategy
from .base import TreeNode


class TreeWalkStrategy(object):
    """
    Defines the walk strategy for the tree.

    TODO: Add more traversal mechanism.
    """
    DEPTH_FIRST = "depth-first"
    BREADTH_FIRST = "breadth-first"


class WalkAPI:
    """
    Implements all the traversal algorithms of the tree.

    TODO: Add more traversal mechanism based on TreeWalkStrategy.
    """

    def __init__(self, strategy: str):
        """
        Initializes the current strategy. Raises InvalidStrategy if invalid.
        :param strategy:
        :type strategy:
        """
        valid_strategies = self.allowed_traversal_strategies()

        if strategy not in valid_strategies:
            raise InvalidWalkStrategy(valid_strategies)
        else:
            self.current_strategy = strategy

    def traverse_dfs_tree_to_dict(self, node: TreeNode, children: list):
        """
        DFS traversal to convert tree to dict

        :param node:
        :type node:
        :param children:
        :type children:
        :return:
        :rtype:
        """

        for child in node.children:
            child_data = {
                TreeNode.NAME: child.name,
                TreeNode.DATA: child.data,
                TreeNode.CHILDREN: []
            }
            children.append(child_data)
            self.traverse_dfs_tree_to_dict(child, child_data[TreeNode.CHILDREN])

    def _traverse_dfs_inorder(self, root_node: TreeNode, callback, *args, **kwargs):
        """
        Run the DFS in-order traversal using recursion.
        :param root_node: Node treated as root for traversal
        :type root_node: instance of TreeNode
        :param callback: callback function to be executed when node is traversed.
        :type callback: method
        :return:
        :rtype:
        """
        # execute callback with node
        callback(root_node, *args, **kwargs)

        # recurse for child
        for child in root_node.children:
            self._traverse_dfs_inorder(child, callback)

    def _traverse_bfs_inorder(self, queue: list, callback, *args, **kwargs):
        """
        Runt the BFS in-order traversal using recursion.
        :param queue: queue containing nodes in order of traversal
        :type queue: list
        :param callback: callback function to be executed when node is traversed.
        :type callback: method
        :return:
        :rtype:
        """

        if len(queue):
            node = queue.pop(0)

            # execute callback (for in-order)
            callback(node, *args, **kwargs)

            for child in node.children:
                queue.append(child)

            self._traverse_bfs_inorder(queue, callback)

    def start_traversal(self, root_node: TreeNode, callback, *args, **kwargs):
        """
        Walk the tree given the root node.
        :param root_node: Node treated as root for traversal
        :type root_node: instance of TreeNode
        :param callback: callback function to be executed when node is traversed.
        :type callback: method
        :return:
        :rtype:
        """

        if self.current_strategy == TreeWalkStrategy.DEPTH_FIRST:
            self._traverse_dfs_inorder(root_node, callback, *args, **kwargs)
        elif self.current_strategy == TreeWalkStrategy.BREADTH_FIRST:
            self._traverse_bfs_inorder([root_node], callback, *args, **kwargs)

    @staticmethod
    def allowed_traversal_strategies():
        """
        Get the valid traversal strategies for the tree.
        :return: list of valid strategies
        :rtype: list
        """
        return [
            TreeWalkStrategy.BREADTH_FIRST,
            TreeWalkStrategy.DEPTH_FIRST
        ]




