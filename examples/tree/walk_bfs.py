from pyds.tree import TreeAPI, TreeWalkStrategy, TreeNodeKeys


name = TreeNodeKeys.NAME
data = TreeNodeKeys.DATA
children = TreeNodeKeys.CHILDREN

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
    api = TreeAPI()
    root = api.parse(tree_data)
    print("Walking - Breadth First")
    api.walk(root, strategy=TreeWalkStrategy.BREADTH_FIRST, callback=print_nodename)


if __name__ == "__main__":
    main()
