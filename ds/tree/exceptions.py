class BaseExceptionTree(Exception):
    """
    Exception baseclass for tree data structure.
    """
    pass


class NodeNotFound(BaseExceptionTree):

    def __init__(self, key):
        """

        :param key: Message to be dis
        :type key: str
        """
        message = "Node %s does not exist." % key
        super(NodeNotFound, self).__init__(message)


class InvalidWalkStrategy(BaseExceptionTree):

    def __init__(self, valid_strategies):
        """

        :param valid_strategies: list of valid strategies
        :type valid_strategies: list
        """

        message = "Invalid walk strategy. Valid strategies are : %s" % ", ".join(valid_strategies)
        super(InvalidWalkStrategy, self).__init__(message)


