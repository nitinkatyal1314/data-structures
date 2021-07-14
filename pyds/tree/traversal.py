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

    def _search(self, node: TreeNode, node_name: str, status: list):
        """
        Search for a node using DFS traversal. The traversal will stop as soon as node is found.

        :param node: the current node which is traversed
        :type node: TreeNode
        :param node_name: name of the node to be searched
        :type node_name: str
        :param status: immutable list to store the status (found / not found)
        :type status: list
        :return:
        :rtype:
        """

        if node.name == node_name:
            status[0] = True
        else:
            for child in node.children:
                self._search(child, node_name, status)

    def search(self, root_node: TreeNode, node_name: str):
        """
        Invokes the search method to find the node given the root node of the tree and the node name.
        :param root_node: Root node of the Tree
        :type root_node: TreeNode
        :param node_name: name of the node
        :type node_name: str
        :return: node is found or not
        :rtype: bool
        """
        status = [False]
        self._search(root_node, node_name, status)
        return status[0]

    def _traverse_dfs_get_height(self, node: TreeNode):
        """
        Recursive method which calculates the height of the child subtree and compares
        with the height of other child subtrees to pick the one with max value.

        :param node: The node of the tree
        :type node: TreeNode
        :return: the height of the tree / subtree
        :rtype: int
        """

        if node.has_children():
            children_height = []
            for child in node.children:
                child_height = self._traverse_dfs_get_height(child)
                child_height += 1
                children_height.append(child_height)

            return max(children_height)

        # base case for leaf node
        else:
            return 0

    def traverse_get_height(self, root_node: TreeNode):
        """
        Invokes the DFR traversal to generate the height of the tree.
        :param root_node: root node of the tree
        :type root_node: TreeNode
        :return: height of the tree
        :rtype: int
        """
        return self._traverse_dfs_get_height(root_node)

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




