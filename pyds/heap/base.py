from .exceptions import DeleteOperationInvalidError, InvalidHeapTypeError


class HeapType:
    """
    Represents the type of heap (min or max)
    """
    MIN = 0
    MAX = 1

    @classmethod
    def validate_type(cls, heap_type: int):
        """
        Validate if the heap type is valid
        :param heap_type:
        :type heap_type:
        :return:
        :rtype:
        """
        if heap_type in [cls.MAX, cls.MIN]:
            return True
        else:
            raise InvalidHeapTypeError([{"type": "MIN", "value": cls.MIN}, {"type": "MAX", "value": cls.MAX}])


class Heap(object):
    """
    The Heap is implemented as an array. Heap hold the following 2 properties:

    1. Parents item value > value of its children (for max heap) [min heap it will be less than]
    2. Heap forms a complete binary tree

    Complete binary tree will have all the level filled except last level, and the leaf nodes
    are filled from left-to-right. Since heap is also a complete binary tree, it can be saved in
    memory as an array with following properties:

    if A = [1,2,3,4,5,6,7] is a heap, with index represented by i (from 0 -> len(A) - 1)
    then children of parent at index i = 2i + 1 & 2i + 2. [or parent for index i is at (i - 1)/ 2]

    Therefore,
    1 has children 2 & 3
    2 has children 4 & 5
    3 has children 6 & 7

    and no children for 4,5,6 & 7
    """

    def __init__(self, of_type: int = HeapType.MAX):
        """
        Initializes an empty heap of type specified (min or max)
        :param of_type:
        :type of_type:
        """
        self.heap = []
        HeapType.validate_type(of_type)
        self.heap_type = of_type

    def heapify_nlogn(self):
        """
        Create method which takes O(nlogn) time. This is different than heapify in sorting where the full
        array is available and we try to make it a heap. Here we maintain heap property as new elements come
        in.

        This procedure assumes that the element added is at the last position and then compares it with the parent
        repeatedly to move the element up the heap. Since for every element we do log(n) comparison
        [or O(h), h is the height of the tree], the overall complexity is O(nlogn).

        :return:
        :rtype:
        """
        last_el_index = len(self.heap) - 1
        current_el_index = last_el_index
        parent_index = int((current_el_index - 1) / 2)

        if self.heap_type == HeapType.MAX:

            # while parent is smaller than current item (for MAX HEAP)
            while self.heap[parent_index] < self.heap[current_el_index]:

                # swap parent with current element
                temp = self.heap[parent_index]
                self.heap[parent_index] = self.heap[current_el_index]
                self.heap[current_el_index] = temp

                # update current element
                current_el_index = parent_index

                # update parent
                parent_index = int((current_el_index - 1) / 2)

        elif self.heap_type == HeapType.MIN:

            # while parent is larger than current item (for MIN HEAP)
            while self.heap[parent_index] > self.heap[current_el_index]:

                # swap parent with current element
                temp = self.heap[parent_index]
                self.heap[parent_index] = self.heap[current_el_index]
                self.heap[current_el_index] = temp

                # update current element
                current_el_index = parent_index

                # update parent
                parent_index = int((current_el_index - 1) / 2)

    def add_node(self, data: int):
        """
        Add data to th heap.
        :param data: The data to be stored in the heap
        :type data:
        :return:
        :rtype:
        """

        # add the data at the last node
        self.heap.append(data)

        # move the data to the rightful location
        self.heapify_nlogn()

    def _get_children_data(self, parent_index):
        """
        Gets the children given the parent index.
        :param parent_index:
        :type parent_index:
        :return:
        :rtype:
        """

        # next child indices if they exist in the heap
        first_child_index = (2 * parent_index) + 1
        second_child_index = (2 * parent_index) + 2

        #  check if first child is there in the heap
        if first_child_index < len(self.heap) - 1:
            children = [
                {"index": first_child_index, "value": self.heap[first_child_index]},
                {"index": second_child_index, "value": self.heap[second_child_index]}
            ] if len(self.heap) - 1 >= second_child_index else \
                [{"index": first_child_index, "value": self.heap[first_child_index]}]

        # no child for this parent
        else:
            children = []

        return children

    def delete_node(self):
        """
        Deletes the root node of the heap (or first element from the list).

        In deletion we delete the first element, then move the last element (to preserve complete tree
        property) to index 0. Now the heap property is maintained by moving the element (at index 0) to the
        bottom [based on MIN / MAX heap] by swapping it with max / min of its children.

        This process takes O(logn) time since moving the element (at index 0) to the rightful place depends
        on the height of the tree. H = O(logn).

        :return: value of the heap node deleted
        :rtype: int
        """

        if len(self.heap) == 0:
            raise DeleteOperationInvalidError()

        if len(self.heap) == 1:
            # remove the item at index 0
            # This is the heap property
            deleted_item = self.heap.pop(0)
            return deleted_item
        else:
            # remove the item at index 0
            # This is the heap property
            deleted_item = self.heap.pop(0)

            # insert the last item in the list at index 0
            # This ensures that tree is complete binary tree
            last_el = self.heap.pop()
            self.heap.insert(0, last_el)
            current_el_index = 0

            children = self._get_children_data(current_el_index)

            # if a max heap
            if self.heap_type == HeapType.MAX:

                while len(children) > 0:
                    max_value = max(map(lambda child: child["value"], children))

                    if max_value > self.heap[current_el_index]:
                        child_with_max_index = list(filter(lambda child: child["value"] == max_value,
                                                           children))[0]["index"]

                        # swap the child with parent
                        temp = self.heap[current_el_index]
                        self.heap[current_el_index] = self.heap[child_with_max_index]
                        self.heap[child_with_max_index] = temp

                        # update the parent
                        current_el_index = child_with_max_index
                        children = self._get_children_data(current_el_index)

                    # break out of the while loop if no children is greater than parent
                    else:
                        break
            elif self.heap_type == HeapType.MIN:

                while len(children) > 0:
                    min_value = min(map(lambda child: child["value"], children))

                    if min_value < self.heap[current_el_index]:
                        child_with_min_index = list(filter(lambda child: child["value"] == min_value,
                                                           children))[0]["index"]

                        # swap the child with parent
                        temp = self.heap[current_el_index]
                        self.heap[current_el_index] = self.heap[child_with_min_index]
                        self.heap[child_with_min_index] = temp

                        # update the parent
                        current_el_index = child_with_min_index
                        children = self._get_children_data(current_el_index)

                    # break out of the while loop if no children is greater than parent
                    else:
                        break

            return deleted_item

    def walk(self, callback):
        """
        Walks the heap in breadth first manner. Iterates through all the items in the list.
        This is O(n).
        :param callback:
        :type callback:
        :return:
        :rtype:
        """

        for item in self.heap:
            callback(item)





