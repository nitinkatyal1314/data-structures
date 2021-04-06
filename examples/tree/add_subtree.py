from ds.tree import Tree

# keys for creating tree dict
name = "name"
data = "data"
children = "children"

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


# method checks if node name is root, adds subtree as a child at index 0
def add_subtree(node):
    if node.name == "root":
        t2 = Tree()
        root_subtree = t2.parse(subtree)
        node.add_children_at_index(0, root_subtree)


# method prints the name of the node
def print_nodename(node):
    print(node.name)


# main method which parse the tree data, calls add_subtree and print_nodename method
def main():
    t1 = Tree()
    t1.parse(tree_data)
    print("Walking Depth First before adding subtree : ")
    t1.walk(print_nodename)
    t1.walk(add_subtree)
    print("Walking Depth First after adding subtree : ")
    t1.walk(print_nodename)


if __name__ == "__main__":
    main()
