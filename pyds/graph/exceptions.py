from common.exceptions import DSBaseException


class NodeDoesNotExist(DSBaseException):

    def __init__(self, key: str):
        """

        Node does not exist error.

        :param key: key name of the node
        :type key: str
        """
        message = "Node with key [%s] does not exist in the graph." % key
        super(NodeDoesNotExist, self).__init__(message)


class AdjacentNodeDoesNotExist(DSBaseException):

    def __init__(self, node: str, adjacent_node: str):
        """

        Node does not exist error.

        :param node: key name of the node
        :type node: str
        :param adjacent_node: key name of the adjacent node
        :type adjacent_node: str
        """
        message = "Node with key [%s] is not an adjacent node to [%s]" % (node, adjacent_node)
        super(AdjacentNodeDoesNotExist, self).__init__(message)


class DuplicateNodeNotAllowed(DSBaseException):

    def __init__(self, key: str):
        """

        Duplicate node is not allowed in the graph.

        :param key: key name of the node
        :type key: str
        """
        message = "Node with key [%s] already exist in the graph." % key
        super(DuplicateNodeNotAllowed, self).__init__(message)


class UnsupportedGraphType(DSBaseException):

    def __init__(self):
        """
        Graph type is not supported.
        """
        message = "Graph type is not supported."
        super(UnsupportedGraphType, self).__init__(message)


class DirectGraphDoesNotSupportAPI(DSBaseException):

    def __init__(self, reason: str):
        """
        Undirected graph does not support this API.
        :param reason: the reason it is not supported.
        :type reason: str
        """
        message = "Directed graph does not support this API - %s ." % reason
        super(DirectGraphDoesNotSupportAPI, self).__init__(message)


class UnDirectGraphDoesNotSupportAPI(DSBaseException):

    def __init__(self, reason: str):
        """
        Undirected graph does not support this API.
        :param reason: the reason it is not supported.
        :type reason: str
        """
        message = "Undirected graph does not support this API - %s ." % reason
        super(UnDirectGraphDoesNotSupportAPI, self).__init__(message)


