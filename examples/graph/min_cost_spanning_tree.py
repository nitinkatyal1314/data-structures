from pyds.graph import GraphAPI, GraphTypes


def run_prims(api, graph_obj):
    """
    Calculates the min cost spanning tree using prim's algorithm.

    :param api: the graph api object
    :type api: GraphAPI
    :param graph_obj: the graph object
    :type graph_obj:
    :return:
    :rtype:
    """

    print("Running Prim's algorithm ... ")

    # generates the dictionary of the format
    # { "tree" : spanning_tree as a dict, "cost" : the actual cost }
    spanning_tree = api.min_cost_spanning_tree_using_prims(graph_obj)
    print(spanning_tree)


def run_kruskal(api, graph_obj):
    """
    Calculates the min cost spanning tree using Kruskal's algorithm.

    :param api: the graph api object
    :type api: GraphAPI
    :param graph_obj: the graph object
    :type graph_obj:
    :return:
    :rtype:
    """

    print("Running Kruskal's algorithm ... ")

    # generates the dictionary of the format
    # { "tree" : spanning_tree as a dict, "cost" : the actual cost }
    spanning_tree = api.min_cost_spanning_tree_using_kruskal(graph_obj)
    print(spanning_tree)


def generate_graph():
    """

    Create a graph and find the min cost spanning tree using Prim's algorithms

    Prim's and Kruskal's algorithm work only with undirected graphs.
    Prim's will not work if graph is disconnected

    :return:
    :rtype:
    """

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

    return api, graph_obj


if __name__ == "__main__":
    api, graph_obj = generate_graph()

    # run prim's
    run_prims(api, graph_obj)
    run_kruskal(api, graph_obj)


