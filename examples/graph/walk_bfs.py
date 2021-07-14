from pyds.graph import GraphAPI, GraphTypes


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
    api.walk_bfs(graph, "A", print_node)


if __name__ == "__main__":
    main()
