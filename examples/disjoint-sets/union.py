from pyds.disjointsets import DisjointSetAPI


def main():
    """
    Example to check if 2 items form a disjoint set and take a union of these set if they are disjoint.

    :return:
    :rtype:
    """

    items = ["A", "B", "C", "D"]
    api = DisjointSetAPI()

    item1 = "A"
    item2 = "B"

    # creates 4 sets each with single item
    api.create(items)

    is_disjoint = api.is_disjoint(item1, item2)

    print("Checking if %s and %s are disjoint sets" % (item1, item2))
    print(is_disjoint)

    print("==========================")
    print("Taking a union of sets now")
    api.union(item1, item2)

    print("==========================")
    print("Checking if post union %s and %s are disjoint sets" % (item1, item2))
    is_disjoint = api.is_disjoint(item1, item2)
    print(is_disjoint)


if __name__ == "__main__":
    main()





