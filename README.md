# Data Structure in Python

This repo contains python implementation of data structures. The following data structures are available:

1. Tree
2. Heap


# Installation

To install from pypi

```bash
pip install py-ds
```

To install from source

```bash
git clone https://github.com/nitinkatyal1314/data-structures.git
python setup.py install
```

# Examples

The examples are available in the examples directory and can be used as a playground or a starting point.

Below are some snippets :

1. Tree creation and traversal (BFS)


```bash
from pyds.tree import Tree


# attributes of the node in the tree
_children = "children"
_name = "name"
_data = "data"

# dictionary representation of tree
tree_data = {
  _name: "R_",
  _data: {},
  _children: [
    {
      _name: "L1",
      _data: {},
      _children: []
    },
    {
      _name: "R1",
      _data: {},
      _children: []
    }
  ]
}


# instantiate the tree
tree = Tree()

# parse the tree
root = tree.parse(tree_data)

# walk callback method, executed for every node that is traversed
def print_nodename(node):
    print(node.name)

# walk the tree (BFS)
# the print_nodename method is passed as a callback while walking
tree.walk(print_nodename, strategy="breadth-first")

```

2. Heap (Insertion and Deletion)

```bash
from pyds.heap import HeapType, Heap

# max heap
heap = Heap(heap_type=HeapType.MAX)

heap.add_node(1)
heap.add_node(2)
heap.add_node(3)
heap.add_node(4)
heap.add_node(5)

# heap print node callback
def print_node(el):
  print("Node : ", el)


# walk the heap
heap.walk(print_node)

# delete the node from the heap
heap.delete_node()
```




