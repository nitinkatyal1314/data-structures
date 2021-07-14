from pyds.graph import GraphAPI, GraphTypes


def main():
    """
    Creates a directed graph and gets all paths from source to destination node.
    The API does not support UNDIRECTED graphs as it may (in most cases) lead to inifinte
    paths.

    :return:
    :rtype:
    """

    # create graph (DIRECTED), add nodes
    # create graph, add nodes
    api = GraphAPI()

    # change this to UnDirected for undirected graphs
    graph = api.init_graph(graph_type=GraphTypes.DIRECTED)

    api.add_node(graph, "A")
    api.add_node(graph, "B")
    api.add_node(graph, "C")
    api.add_node(graph, "D")
    api.add_node(graph, "E")
    api.add_node(graph, "F")

    # connect nodes in graph
    # connect nodes in graph
    api.add_edge(graph, "A", "B")
    api.add_edge(graph, "A", "C")
    api.add_edge(graph, "C", "B")
    api.add_edge(graph, "B", "D")
    api.add_edge(graph, "D", "F")
    api.add_edge(graph, "C", "E")
    api.add_edge(graph, "E", "F")
    api.add_edge(graph, "D", "E")

    source_node = "A"
    destination_node = "F"
    print("Finding all paths from %s -> %s" % (source_node, destination_node))

    paths = api.get_paths_to_node(graph, destination_node, source_node)
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
