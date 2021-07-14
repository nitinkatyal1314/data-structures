from pyds.graph import GraphAPI, GraphTypes


def main():
    """

    Create a graph and run Dijikstra algorithm to find shortest path to all the nodes
    from the source node.

    Dijikstra algorithm does not work with negative weights.

    :return:
    :rtype:
    """

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


if __name__ == "__main__":
    main()
