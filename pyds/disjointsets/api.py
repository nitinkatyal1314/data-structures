from .base import DisjointSets
from .exceptions import DisjointSetEmpty


class DisjointSetAPI(object):
    """
    API for disjoint set.
    """

    def __init__(self,):
        """
        Initializes the set

        """
        self.set = None

    def create(self, items: list):
        """
        Creates a disjoint set from the list of items
        :param items: the list of items (str) for which the set is to be created
        :type items: list
        :return:
        :rtype:
        """

        self.set = DisjointSets(items)

    def is_disjoint(self, item1: str, item2: str):
        """
        Checks if the item1 and item2 forms a disjoint set.

        :param item1: the first item from the set
        :type item1: str
        :param item2: the seconds item from the set
        :type item2: str
        :return: whether items make a disjoint set or not
        :rtype: bool
        """
        if self.set is not None:
            return self.set.is_disjoint(item1, item2)

        else:
            raise DisjointSetEmpty()

    def union(self, item1, item2):
        """
        Take union of disjoint sets for item1 and item2.

        :param item1: the first item from the set
        :type item1: str
        :param item2: the seconds item from the set
        :type item2: str
        :return:
        :rtype:
        """

        if self.set is not None:
            self.set.union(item1, item2)
        else:
            raise DisjointSetEmpty()


