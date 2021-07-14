from .base import DirectedGraph, UnDirectedGraph, Graph
from .exceptions import UnsupportedGraphType, UnDirectGraphDoesNotSupportAPI, DirectGraphDoesNotSupportAPI


class GraphTypes(object):
    DIRECTED = "directed"
    UNDIRECTED = "undirected"


class GraphAPI(object):
    """
    Graph API to expose graph data structure.

    TODO: All method are staticmethod.
    """

    def init_graph(self, graph_type: GraphTypes = GraphTypes.DIRECTED):
        """
        Initialize the graph of the given type.

        :param graph_type: the type of the graph
        :type graph_type: GraphTypes
        :return: graph instance
        :rtype: DirectedGraph
        """

        if graph_type == GraphTypes.DIRECTED:
            graph_obj = DirectedGraph()
        elif graph_type == GraphTypes.UNDIRECTED:
            graph_obj = UnDirectedGraph()
        else:
            raise UnsupportedGraphType()

        return graph_obj

    def add_node(self, graph: DirectedGraph, key: str, attr: dict = None):
        """
        Add a node given its key and the attributes.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :param key: The unique key for the graph
        :type key: str
        :param attr: Attributes of the node (means to add custom data for a node)
        :type attr: dict
        :return:
        :rtype:
        """

        graph.add_node(key, attr)

    def get_all_nodes(self, graph: DirectedGraph):
        """
        Get all nodes of the graph.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :return: list of all nodes in graph
        :rtype: list
        """

        return graph.get_all_nodes()

    def count_edges(self, graph: DirectedGraph):
        """
        Get the count of number of edges in graph.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :return: the number of edges in graph
        :rtype: int
        """
        return graph.get_total_edges()

    def as_dict(self, graph: DirectedGraph):
        """
        Retrieves the graph as dictionary.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :return: get graph as a dictionary
        :rtype: dict
        """

        return graph.as_dict()

    def add_edge(self, graph: DirectedGraph, source: str, destination: str, weight: float = 0.0):
        """
        Add edge between two nodes. Use this method to connect two nodes of the same
        graph.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :param source: source node to connect
        :type source: str
        :param destination: destination node to connect
        :type destination: str
        :param weight: weight of the connected edge
        :type weight: float
        :return:
        :rtype:
        """
        graph.add_edge(source, destination, weight)

    def connect_graph(self, graph: DirectedGraph, to_graph: DirectedGraph, source: str, destination: str, weight: float = 0.0):
        """
        Connect two nodes given their key and the weight.
        Use this method to connect two nodes of different graph.
        Post this operation the two graphs will loose their individual state and be treated as one,
        so both the source and destination graph will be the same.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :param to_graph: destination graph to connect with.
        :type to_graph: Graph
        :param source: which node to use when connecting from source
        :type source: str
        :param destination: which node to use when connecting to destination
        :type destination: str
        :param weight: weight of the edge, default to 0.0
        :type weight: float
        :return:
        :rtype:
        """
        graph.connect_graph(to_graph, source, destination, weight)

    def adjacent_nodes(self, graph: DirectedGraph, node: str, only_names: bool = True):
        """
        Returns the list of adjacent node for the given node.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :param node: node for which adjacent nodes needs to be retrieved
        :type node: str
        :param only_names: Whether to retrieve only node names or weight data as well (default to True)
        :type only_names: bool
        :return: list of adjacent graph nodes
        :rtype: list
        """

        return graph.find_adjacent_nodes(node, only_names)

    def get_paths_to_node(self, graph: DirectedGraph, destination: str, source: str):
        """
        Get all paths to a node in the graph given the starting node.
        This will include shortest path as well as longest paths, and everything in between.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :param destination: The node to which the path needs to be evaluated
        :type destination: str
        :param source: The starting node to trace the path
        :type source: str
        :return: list of strings (each depicting comma separated nodes) to all paths
        :rtype: list
        """

        # TODO: Add path depth parameter to converge infinite paths to finite
        if isinstance(graph, UnDirectedGraph):
            raise UnDirectGraphDoesNotSupportAPI(reason="The graph may lead to infinite paths")

        return graph.get_all_paths_to_node(destination, source)

    def has_loop(self, graph: DirectedGraph):
        """
        Check if graph has loops.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :return: True / False if graph has loop, and the nodes which form the loop
        :rtype: tuple
        """
        return graph.has_loop()

    def find_shortest_path_using_dijikstra(self, graph: DirectedGraph, start_node):
        """
        Find the shortest path to all the nodes using dijikstra given the source node.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :param start_node: The source node to find the paths
        :type start_node: str
        :return: dictionary containing path to all nodes from source node
        :rtype: dict
        """

        return graph.run_dijikstra(start_node)

    def walk_dfs(self, graph: DirectedGraph, start_node: str, callback):
        """
        Walk in DFS manner given the start node. We use recursive implementation though iterative is available as well.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :param start_node: use the node as the starting point
        :type start_node: str
        :param callback: Callback method to execute when visiting a node
        :type callback: function
        :return:
        :rtype:
        """

        graph.walk_dfs_recursive(start_node, [], callback)

    def walk_bfs(self, graph: DirectedGraph, start_node: str, callback):
        """
        Walk in BFS manner given the start node. We use recursive implementation though iterative is available as well.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :param start_node: use the node as the starting point
        :type start_node: str
        :param callback: Callback method to execute when visiting a node
        :type callback: function
        :return:
        :rtype:
        """
        graph.walk_bfs_recursive([start_node], [], callback)

    def min_cost_spanning_tree_using_prims(self, graph: UnDirectedGraph):
        """
        Generate min cost spanning tree using prim's algorithms.

        :param graph: Graph instance
        :type graph: DirectedGraph
        :return: spanning tree as a dictionary
        :rtype: dict
        """

        if isinstance(graph, UnDirectedGraph):
            spanning_tree = graph.generate_minimum_cost_spanning_tree_using_prims()
            return spanning_tree
        else:
            raise DirectGraphDoesNotSupportAPI("Directed graphs does not support this API.")

    def min_cost_spanning_tree_using_kruskal(self, graph: UnDirectedGraph):
        """
        Generate min cost spanning tree using prim's algorithms.

        :return: spanning tree as a dictionary
        :rtype: dict
        """

        if isinstance(graph, UnDirectedGraph):
            spanning_tree = graph.generate_minimum_cost_spanning_tree_using_kruskal()
            return spanning_tree
        else:
            raise DirectGraphDoesNotSupportAPI("Directed graphs does not support this API.")











