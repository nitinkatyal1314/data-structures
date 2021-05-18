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

3. Graph (Creation and DFS Walk)

```bash
from pyds.graph import Graph, GraphTypes

# create graph (UNDIRECTED / DIRECTED), add nodes
graph = Graph(graph_type=GraphTypes.UNDIRECTED)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")

# connect nodes in graph
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("C", "B")
graph.add_edge("B", "D")
graph.add_edge("D", "F")
graph.add_edge("C", "E")
graph.add_edge("E", "F")


# graph print node callback
def print_node(node):
  print("Node : ", node)
  
# walk graph using DFS (start from node A)
graph.walk_dfs("A", print_node)

```

4. Graph (Dijikstra - Single source shortest path)

```bash


# create graph, add nodes
graph = Graph(graph_type=GraphTypes.DIRECTED)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")

# connect nodes in graph and provide weights for the edge
graph.add_edge("A", "B", 5.0)
graph.add_edge("A", "C", 2.0)
graph.add_edge("B", "D", 3.0)
graph.add_edge("B", "C", 9.0)
graph.add_edge("C", "E", 5.0)
graph.add_edge("E", "D", 4.0)
graph.add_edge("E", "F", 6.0)
graph.add_edge("D", "F", 1.0)

# source node
source_node = "A"

# run dijikstra, and print results
shortest_distance_data = graph.find_shortest_path_using_dijikstra(start_node=source_node)
print(shortest_distance_data)

```




