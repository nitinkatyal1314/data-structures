from pyds.graph import Graph, GraphTypes


def main():
    """

    Create a graph and run Dijikstra algorithm to find shortest path to all the nodes
    from the source node.

    Dijikstra algorithm does not work with negative weights.

    :return:
    :rtype:
    """

    # create graph, add nodes
    graph = Graph(graph_type=GraphTypes.DIRECTED)
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_node("F")

    # connect nodes in graph
    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "D", 3)
    graph.add_edge("B", "C", 9)
    graph.add_edge("C", "E", 5)
    graph.add_edge("E", "D", 4)
    graph.add_edge("E", "F", 6)
    graph.add_edge("D", "F", 1)

    source_node = "A"

    print("Running Dijikstra algorithm ... ")
    shortest_distance_data = graph.find_shortest_path_using_dijikstra(start_node=source_node)
    print("Shortest distance to all nodes from source node [%s] is: " % source_node)
    print(shortest_distance_data)


if __name__ == "__main__":
    main()
