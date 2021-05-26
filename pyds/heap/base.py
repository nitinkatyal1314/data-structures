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

        :param of_type: type of the heap (MIN / MAX)
        :type of_type: int
        """
        self.heap = []
        HeapType.validate_type(of_type)
        self.heap_type = of_type

    def get_heap(self):
        """
        Returns the heap array.
        """
        return self.heap

    def create_heap(self, arr: list):
        """
        Create heap from an array.

        :param arr: type of the heap (MIN / MAX)
        :type arr: int
        """

        # lets assume that arr is already a heap
        # then heapify it
        self.heap = arr

        # list length
        n = len(arr)

        # No need to process the leaf nodes
        # so we can start with their parent and move backward
        # the heapify method will recurse to adjust the position of the element
        start_index = int((n / 2) - 1)

        while start_index >= 0:
            self.heapify_n(arr, n, start_index)
            start_index -= 1

        # the list is now a heap
        self.heap = arr

    def heapify_n(self, arr: list, n: int, current_index: int):
        """
        Efficient way to create heap given the array. Heapify is different than adding a node
        in the heap in the sense that heapify will create heap in backward direction from
        array and maintain the heap property by moving the node down the tree to its rightful place.

        For heapify the maximum number of moves will happen for the node at the top (which is very less, only 1 if root)
        and will be of the order of the height of the tree [imagine a root node going to the leaf]. This is in contrast
        to the heap add_node method, which will add the node as the leaf and move it upwards. Given the number
        of leaf nodes in a tree is larger than the top nodes (or root), the average case for heapify will be much faster.

        ** In a tree if an algorithms reduces the number of operations at the bottom nodes, then it is more efficient
        because most of the nodes lie at the bottom. For example

        A complete binary tree will have nodes
            h = 0 (root) = 1 (or 2^0)
            h = 1 (level 1) = 2 (or 2^1)
            h = 3 (level 2) = 2^2


        Therefore total nodes = 2^0+2^1+2^3+.......+2^h (where h is the height)
        This sum is a GP series (a = 1, r = 2), a(r^(h+1) - 1)/ (r - 1) = 2^(h+1) - 1

            n = 2^(h+1) - 1

        We can approximate this number as n ~ 2^(h+1)

        Consider the last 3 levels only, approximate number of nodes are ~ 2^h + 2^(h-1) + 2^(h-2)
            replace n ~ 2^(h+1)

            total nodes (last 3 level) = n/2 + n/4 + n/8 ~ 0.875n

            So almost 87% of the nodes are at the bottom 3 level and an algorithm reducing number
            of operations at bottom nodes will perform better.

        For more info on O(n) for heapify, read this :
        http://www.cs.umd.edu/%7Emeesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf

        """
        # current index is the parent
        parent_index = current_index
        children = self._get_children_data(parent_index)

        if len(children) > 0:

            if self.heap_type == HeapType.MAX:
                max_value = max(map(lambda child: child["value"], children))
                child_with_max_index = list(filter(lambda child: child["value"] == max_value,
                                                   children))[0]["index"]

                if arr[current_index] < max_value:
                    parent_index = child_with_max_index

            elif self.heap_type == HeapType.MIN:
                min_value = min(map(lambda child: child["value"], children))
                child_with_min_index = list(filter(lambda child: child["value"] == min_value,
                                                   children))[0]["index"]

                if arr[current_index] > min_value:
                    parent_index = child_with_min_index

        # check if parent index has changed in the process
        if parent_index != current_index:
            # swap the parent with the child
            temp = arr[current_index]
            arr[current_index] = arr[parent_index]
            arr[parent_index] = temp

            # recurse
            self.heapify_n(arr, n, parent_index)

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
        :type data: int
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





