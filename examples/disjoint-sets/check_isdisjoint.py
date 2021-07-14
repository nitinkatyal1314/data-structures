from pyds.disjointsets import DisjointSetAPI


def main():
    """
    Example to create a disjoint set, and check if 2 items they are disjoint.

    :return:
    :rtype:
    """

    items = ["A", "B", "C", "D"]
    api = DisjointSetAPI()

    # creates 4 sets each with single item
    api.create(items)

    print("Checking if A and B are disjoint sets")
    print(api.is_disjoint("A", "B"))


if __name__ == "__main__":
    main()




