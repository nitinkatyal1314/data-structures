from pyds.heap import HeapType, Heap


def print_node(el: int):
    """
    Prints the node
    :param el: node value
    :type el: int
    :return:
    :rtype:
    """
    print("Node : ", el)


def playground():

    # creates a max heap
    heap = Heap()
    print("Adding Node : ", 1)
    heap.add_node(1)
    heap.walk(print_node)
    print("Adding Node : ", 2)
    heap.add_node(2)
    heap.walk(print_node)
    print("Adding Node : ", 3)
    heap.add_node(3)
    heap.walk(print_node)
    print("Adding Node : ", 4)
    heap.add_node(4)
    heap.walk(print_node)
    print("Adding Node : ", 5)
    heap.add_node(5)
    heap.walk(print_node)

    print("Deletion Start")

    node = heap.delete_node()
    print("Deleted element ", node)
    heap.walk(print_node)

    node = heap.delete_node()
    print("Deleted element ", node)
    heap.walk(print_node)

    node = heap.delete_node()
    print("Deleted element ", node)
    heap.walk(print_node)

    node = heap.delete_node()
    print("Deleted element ", node)
    heap.walk(print_node)

    node = heap.delete_node()
    print("Deleted element ", node)
    heap.walk(print_node)

    node = heap.delete_node()
    print("Deleted element ", node)
    heap.walk(print_node)


if __name__ == "__main__":
    playground()
