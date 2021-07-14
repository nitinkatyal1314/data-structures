from common.exceptions import DSBaseException


class DisjointSetEmpty(DSBaseException):
    """
    Disjoint set is empty error.
    """

    def __init__(self):
        """
        Raises disjoint set empty error when invoked
        """
        message = "Empty set. Make sure that set has been populated with all the items"
        super(DisjointSetEmpty, self).__init__(message)


class NodeNotFoundInSet(DSBaseException):
    """
    Not not found in the set.
    """

    def __init__(self, node_name):
        """

        :param node_name: name of the node
        :type node_name: str
        """

        message = "Node %s not found in the set" % node_name
        super(NodeNotFoundInSet, self).__init__(message)
