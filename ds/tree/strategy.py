class TreeWalkStrategy(object):
    """
    Defines the walk strategy for the tree
    """
    IN_ORDER = "in-order"
    POST_ORDER = "post-order"
    BREADTH_FIRST = "breadth-first"

    @classmethod
    def get_valid_strategies(cls):
        """
        Get the valid traversal strategies
        :return: list of valid strategies
        :rtype: list
        """

        return [cls.IN_ORDER, cls.POST_ORDER, cls.BREADTH_FIRST]
