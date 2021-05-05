from .base import Heap, HeapType


class HeapAPI(object):
    """
    The heap API to interact with heap. Allow folloring operation:

    1. Create heap MIN / MAX
    2. Delete from heap
    3. Traverse the heap

    """

    def __init__(self, heap_type: int = HeapType.MAX):
        """
        Initializes the Heap
        :param heap_type: type of heap [MIN (0) / MAX (1)]
        :type heap_type: int
        """
        self.heap_obj = Heap(heap_type)

    def get_heap_as_array(self):
        """
        Returns the heap.
        """

        return self.heap_obj.get_heap()

    def create_heap_from_array(self, arr: list):
        """
        Create heap from an array.
        :param arr: list of items from which heap is to be created
        :type arr: int
        """

        self.heap_obj.create_heap(arr)
        return self.get_heap_as_array()

    def add_node(self, data: int):
        """
        Adds data to the heap.
        :param data: data
        :type data: int
        :return:
        :rtype:
        """

        self.heap_obj.add_node(data)

    def delete_node(self):
        """
        Deletes root element from the heap.
        :return: data
        :rtype: int
        """
        return self.heap_obj.delete_node()

    def walk(self, callback):
        """
        Walks the heap and execute callback when traversing the heap.
        :param callback:
        :type callback:
        :return:
        :rtype:
        """
        self.heap_obj.walk(callback)
