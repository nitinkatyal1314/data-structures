from ds.tree import Tree


name = "name"
data = "data"
children = "children"

tree_data = {
    name: "root",
    data: {},
    children: [
        {
            name: "L1",
            children: [
                {
                    name: "L2-1",
                    data: {},
                    children: []
                },
                {
                    name: "L2-2",
                    data: {},
                    children: []
                }
            ],
            data: {}
        },
{
            name: "R1",
            children: [],
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
