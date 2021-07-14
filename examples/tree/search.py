from pyds.tree import TreeAPI, TreeNodeKeys


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


def main():
    api = TreeAPI()
    root = api.parse(tree_data)
    search_for_node = "R2-1"
    print("Searching for node - %s" % search_for_node)
    found = api.has_node(root, search_for_node)
    if found:
        print("Node %s found in the tree." % search_for_node)
    else:
        print("Node %s not found in the tree." % search_for_node)


if __name__ == "__main__":
    main()
