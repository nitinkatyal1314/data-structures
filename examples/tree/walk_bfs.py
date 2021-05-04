from pyds.tree import Tree


name = "name"
data = "data"
children = "children"

tree_data = {
    name: "R_",
    data: {},
    children: [
        {
            name: "L1",
            children: [
                {
                    name: "L2-1",
                    data: {},
                    children: [
                        {
                            name: "L3-1",
                            data: {},
                            children: []
                        },
                    ]
                },
                {
                    name: "L2-2",
                    data: {},
                    children: []
                },
                {
                    name: "L2-3",
                    data: {},
                    children: []
                },

            ],
            data: {}
        },
        {
            name: "R1",
            children: [
                {
                    name: "R2-1",
                    data: {},
                    children: []
                },
            ],
            data: {}
        }
    ]
}


def print_nodename(node):
    print(node.name)


def main():
    tree = Tree()
    root = tree.parse(tree_data)
    print("Walking - Breadth First")
    tree.walk(print_nodename, strategy="breadth-first")


if __name__ == "__main__":
    main()
