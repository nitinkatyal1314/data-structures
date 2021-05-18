from pyds.graph import Graph, GraphTypes


def main():
    """
    Create a graph and check if there is a loop in it. Also
    print the nodes forming a loop.

    The has_loop API does not print all the loops but the first one detected.
    This is to save in computation work when the purpose is just to detect
    if there is a loop.

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

    # connect nodes in graph
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "B")
    graph.add_edge("D", "C")
    graph.add_edge("D", "E")

    print("Checking if graph has loops...")
    loop_data = graph.has_loop()
    if loop_data[0]:
        print("Loop Detected is : ", loop_data[1])
    else:
        print("No Loop detected.")


if __name__ == "__main__":
    main()
