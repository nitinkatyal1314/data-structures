from pyds.tree import TreeAPI, TreeNodeKeys, TreeWalkStrategy

# keys for creating tree dict
name = TreeNodeKeys.NAME
data = TreeNodeKeys.DATA
children = TreeNodeKeys.CHILDREN

# subtree
subtree = {
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
}

# tree
tree_data = {
    name: "root",
    data: {},
    children: [
        {
            name: "R1",
            children: [],
            data: {}
        }
    ]
}


# method prints the name of the node
def print_nodename(node):
    print(node.name)


# main method which parse the tree data, calls add_subtree and print_nodename method
def main():
    api = TreeAPI()
    root1 = api.parse(tree_data)
    print("Walking Depth First before adding subtree : ")
    api.walk(root1, strategy=TreeWalkStrategy.DEPTH_FIRST, callback=print_nodename)

    root2 = api.parse(subtree)
    root1.add_children_at_index(0, root2)
    print("Walking Depth First after adding subtree : ")
    api.walk(root1, strategy=TreeWalkStrategy.DEPTH_FIRST, callback=print_nodename)


if __name__ == "__main__":
    main()
