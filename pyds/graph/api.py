from .base import DirectedGraph, UnDirectedGraph, Graph
from .exceptions import UnsupportedGraphType, UnDirectGraphDoesNotSupportAPI


class GraphTypes(object):
    DIRECTED = "directed"
    UNDIRECTED = "undirected"


class GraphAPI(object):
    """
    Graph API to expose graph data structure.
    """

    def __init__(self, graph_type: GraphTypes = GraphTypes.DIRECTED):
        """
        Initialize the API with the type of graph.

        :param graph_type: Type of graph (directed / undirected)
        :type graph_type: GraphTypes
        """
        self.graph_type = graph_type
        if graph_type == GraphTypes.DIRECTED:
            self.graph_obj = DirectedGraph()
        elif graph_type == GraphTypes.UNDIRECTED:
            self.graph_obj = UnDirectedGraph()
        else:
            raise UnsupportedGraphType()

    def add_node(self, key: str, attr: dict = None):
        """
        Add a node given its key and the attributes.

        :param key: The unique key for the graph
        :type key: str
        :param attr: Attributes of the node (means to add custom data for a node)
        :type attr: dict
        :return:
        :rtype:
        """

        self.graph_obj.add_node(key, attr)

    def get_all_nodes(self):
        """
        Get all nodes of the graph.
        :return: list of all nodes in graph
        :rtype: list
        """

        return self.graph_obj.get_all_nodes()

    def as_dict(self):
        """
        Retrieves the graph as dictionary.

        :return: get graph as a dictionary
        :rtype: dict
        """

        return self.graph_obj.as_dict()

    def add_edge(self, source: str, destination: str, weight: float = 0.0):
        """
        Add edge between two nodes. Use this method to connect two nodes of the same
        graph.

        :param source: source node to connect
        :type source: str
        :param destination: destination node to connect
        :type destination: str
        :param weight: weight of the connected edge
        :type weight: float
        :return:
        :rtype:
        """
        self.graph_obj.add_edge(source, destination, weight)

    def connect_graph(self, to_graph: Graph, source: str, destination: str, weight: float = 0.0):
        """
        Connect two nodes given their key and the weight.
        Use this method to connect two nodes of different graph.
        Post this operation the two graphs will loose their individual state and be treated as one,
        so both the source and destination graph will be the same.

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
        self.graph_obj.connect_graph(to_graph, source, destination, weight)

    def adjacent_nodes(self, node: str, only_names: bool = True):
        """
        Returns the list of adjacent node for the given node.

        :param node: node for which adjacent nodes needs to be retrieved
        :type node: str
        :param only_names: Whether to retrieve only node names or weight data as well (default to True)
        :type only_names: bool
        :return: list of adjacent graph nodes
        :rtype: list
        """

        return self.graph_obj.find_adjacent_nodes(node, only_names)

    def get_paths_to_node(self, destination: str, source: str):
        """
        Get all paths to a node in the graph given the starting node.
        This will include shortest path as well as longest paths, and everything in between.

        :param destination: The node to which the path needs to be evaluated
        :type destination: str
        :param source: The starting node to trace the path
        :type source: str
        :return: list of strings (each depicting comma separated nodes) to all paths
        :rtype: list
        """

        # TODO: Add path depth parameter to converge infinite paths to finite
        if self.graph_type == GraphTypes.UNDIRECTED:
            raise UnDirectGraphDoesNotSupportAPI(reason="The graph may lead to infinite paths")

        return self.graph_obj.get_all_paths_to_node(destination, source)

    def has_loop(self):
        """
        Check if graph has loops.

        :return: True / False if graph has loop, and the nodes which form the loop
        :rtype: tuple
        """
        return self.graph_obj.has_loop()

    def find_shortest_path_using_dijikstra(self, start_node):
        """
        Find the shortest path to all the nodes using dijikstra given the source node.

        :param start_node: The source node to find the paths
        :type start_node: str
        :return: dictionary containing path to all nodes from source node
        :rtype: dict
        """

        return self.graph_obj.run_dijikstra(start_node)

    def walk_dfs(self, start_node: str, callback):
        """
        Walk in DFS manner given the start node. We use recursive implementation though iterative is available as well.
        :param start_node: use the node as the starting point
        :type start_node: str
        :param callback: Callback method to execute when visiting a node
        :type callback: function
        :return:
        :rtype:
        """

        self.graph_obj.walk_dfs_recursive(start_node, [], callback)

    def walk_bfs(self, start_node: str, callback):
        """
        Walk in BFS manner given the start node. We use recursive implementation though iterative is available as well.
        :param start_node: use the node as the starting point
        :type start_node: str
        :param callback: Callback method to execute when visiting a node
        :type callback: function
        :return:
        :rtype:
        """
        self.graph_obj.walk_bfs_recursive([start_node], [], callback)










