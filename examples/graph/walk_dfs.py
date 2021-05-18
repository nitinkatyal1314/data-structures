from pyds.graph import Graph, GraphTypes


def print_node(node):
    """
    Callback function to print the node.

    :param node: node of the graph
    :type node: str
    :return:
    :rtype:
    """
    print("Node : ", node)


def main():
    """
    Creates a undirected graph and traverse the nodes using Depth-First traversal API.

    :return:
    :rtype:
    """

    # create graph, add nodes
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

    print("DFS Start ")
    graph.walk_dfs("A", print_node)


if __name__ == "__main__":
    main()
