from ds.tree import Tree


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
                            name: "L3-L2-1-1",
                            data: {},
                            children: []
                        },
                        {
                            name: "L3-L2-1-2",
                            data: {},
                            children: []
                        },
                    ]
                },
                {
                    name: "L2-2",
                    data: {},
                    children: [
                        {
                            name: "L3-L2-2-1",
                            data: {},
                            children: []
                        },
                    ]
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
    print("Walking - Depth First")
    tree.walk(print_nodename)


if __name__ == "__main__":
    main()
