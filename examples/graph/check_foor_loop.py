from pyds.graph import GraphAPI, GraphTypes


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
    api = GraphAPI()

    # change this to Directed for directed graphs
    graph = api.init_graph(graph_type=GraphTypes.UNDIRECTED)

    # create graph, add nodes
    api.add_node(graph, "A")
    api.add_node(graph, "B")
    api.add_node(graph, "C")
    api.add_node(graph, "D")
    api.add_node(graph, "E")

    # connect nodes in graph
    api.add_edge(graph, "B", "A")
    api.add_edge(graph, "A", "D")
    api.add_edge(graph, "E", "B")
    api.add_edge(graph, "B", "C")
    api.add_edge(graph, "D", "E")

    print("Checking if graph has loops...")
    loop_data = api.has_loop(graph)
    if loop_data[0]:
        print("Loop Detected is : ", loop_data[1])
    else:
        print("No Loop detected.")


if __name__ == "__main__":
    main()
