# Data Structure in Python

This repo contains python implementation of data structures. The following data structures are available:

1. Tree
2. Heap
3. Disjoint sets
4. Graph


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

## Tree creation and traversal (BFS)


```python
from pyds.tree import TreeAPI, TreeWalkStrategy, TreeNodeKeys


name = TreeNodeKeys.NAME
data = TreeNodeKeys.DATA
children = TreeNodeKeys.CHILDREN

# tree as JSON with root node and 2 children (L1 and R1), and R2-1 is the child of R1
# if the tree is large, it is recommended to create smaller subtrees and use the add_child API
# refer examples/tree/add_subtree.py for the API
tree_data = {
    name: "R_",
    data: {},
    children: [
        {
            name: "L1",
            children: [],
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

# callback methof to print the node
def print_nodename(node):
    print(node.name)

# the main API
def main():
    api = TreeAPI()
    root = api.parse(tree_data)
    print("Walking - Breadth First")
    api.walk(root, strategy=TreeWalkStrategy.BREADTH_FIRST, callback=print_nodename)


# run the main method
main()
```

## Heap (Insertion and Deletion)

```python
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

## Disjoint set (check items are disjoint)

```python
from pyds.disjointsets import DisjointSetAPI

items = ["A", "B", "C", "D"]
api = DisjointSetAPI()

item1 = "A"
item2 = "B"

# creates 4 sets each with single item
api.create(items)

is_disjoint = api.is_disjoint(item1, item2)

print("Checking if %s and %s are disjoint sets" % (item1, item2))
print(is_disjoint)

print("==========================")
print("Taking a union of sets now")
api.union(item1, item2)

print("==========================")
print("Checking if post union %s and %s are disjoint sets" % (item1, item2))
is_disjoint = api.is_disjoint(item1, item2)
print(is_disjoint)

```


## Graph (Creation and DFS Walk)

```python
from pyds.graph import GraphAPI, GraphTypes

# callback method to print the node during traversal
def print_node(node):
    """
    Callback function to print the node.

    :param node: node of the graph
    :type node: str
    :return:
    :rtype:
    """
    print("Node : ", node)

# create graph, add nodes
api = GraphAPI()

# change this to Directed for directed graphs
graph = api.init_graph(graph_type=GraphTypes.UNDIRECTED)

api.add_node(graph, "A")
api.add_node(graph, "B")
api.add_node(graph, "C")
api.add_node(graph, "D")
api.add_node(graph, "E")
api.add_node(graph, "F")

# connect nodes in graph
api.add_edge(graph, "A", "B")
api.add_edge(graph, "A", "C")
api.add_edge(graph, "C", "B")
api.add_edge(graph, "B", "D")
api.add_edge(graph, "D", "F")
api.add_edge(graph, "C", "E")
api.add_edge(graph, "E", "F")

print("DFS Start ")
api.walk_dfs(graph, "A", print_node)

```

## Graph (Dijikstra - Single source shortest path)

```python
from pyds.graph import GraphAPI, GraphTypes

# create graph (DIRECTED), add nodes
# create graph, add nodes
api = GraphAPI()
graph = api.init_graph(graph_type=GraphTypes.DIRECTED)

api.add_node(graph, "A")
api.add_node(graph, "B")
api.add_node(graph, "C")
api.add_node(graph, "D")
api.add_node(graph, "E")
api.add_node(graph, "F")

# connect nodes in graph
api.add_edge(graph, "A", "B", 5)
api.add_edge(graph, "A", "C", 2)
api.add_edge(graph, "B", "D", 3)
api.add_edge(graph, "B", "C", 9)
api.add_edge(graph, "C", "E", 5)
api.add_edge(graph, "E", "D", 4)
api.add_edge(graph, "E", "F", 6)
api.add_edge(graph, "D", "F", 1)

source_node = "A"

print("Running Dijikstra algorithm starting from node %s. " % source_node)
shortest_distance_data = api.find_shortest_path_using_dijikstra(graph, start_node=source_node)
print("Shortest distance to all nodes from source node [%s] is: " % source_node)
print(shortest_distance_data)

```

## Minimum cost spanning Tree (Prim's and Kruskal)

```python
from pyds.graph import GraphAPI, GraphTypes

# create graph, add nodes
api = GraphAPI()

graph_obj = api.init_graph(graph_type=GraphTypes.UNDIRECTED)

api.add_node(graph_obj, "A")
api.add_node(graph_obj, "B")
api.add_node(graph_obj, "C")
api.add_node(graph_obj, "D")
api.add_node(graph_obj, "E")
api.add_node(graph_obj, "F")
api.add_node(graph_obj, "G")

# connect nodes in graph
api.add_edge(graph_obj, "A", "B", 10)
api.add_edge(graph_obj, "A", "C", 28)
api.add_edge(graph_obj, "B", "E", 25)
api.add_edge(graph_obj, "E", "D", 24)
api.add_edge(graph_obj, "E", "F", 22)
api.add_edge(graph_obj, "C", "D", 14)
api.add_edge(graph_obj, "C", "G", 16)
api.add_edge(graph_obj, "F", "D", 18)
api.add_edge(graph_obj, "F", "G", 12)

spanning_tree = api.min_cost_spanning_tree_using_prims(graph_obj)
print(spanning_tree)
```




