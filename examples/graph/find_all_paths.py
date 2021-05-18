from pyds.graph import Graph, GraphTypes


def main():
    """
    Creates a directed graph and gets all paths from source to destination node.
    The API does not support UNDIRECTED graphs as it may (in most cases) lead to inifinte
    paths.

    :return:
    :rtype:
    """

    # create graph (DIRECTED), add nodes
    graph = Graph(graph_type=GraphTypes.DIRECTED)
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
    graph.add_edge("D", "E")

    print("Finding all paths...")
    source_node = "A"
    destination_node = "F"
    paths = graph.get_paths_to_node(destination_node, source_node)
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
