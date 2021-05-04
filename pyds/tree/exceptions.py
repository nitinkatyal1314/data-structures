from common.exceptions import DSBaseException


class NodeNotFound(DSBaseException):

    def __init__(self, key):
        """

        :param key: Message to be dis
        :type key: str
        """
        message = "Node %s does not exist." % key
        super(NodeNotFound, self).__init__(message)


class InvalidWalkStrategy(DSBaseException):

    def __init__(self, valid_strategies):
        """

        :param valid_strategies: list of valid strategies
        :type valid_strategies: list
        """

        message = "Invalid walk strategy. Valid strategies are : %s" % ", ".join(valid_strategies)
        super(InvalidWalkStrategy, self).__init__(message)


