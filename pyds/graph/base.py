import sys
from .exceptions import NodeDoesNotExist, DuplicateNodeNotAllowed, AdjacentNodeDoesNotExist
from pyds.disjointsets import DisjointSetAPI


class Graph(object):
    """
    Base class of the Graph.
    """

    def as_dict(self):
        """
        Gets graph as dict.
        :return:
        :rtype:
        """

        return {}


class DirectedGraph(Graph):
    """

    This is the main class for Directed Graph. This will be used as a base class
    for the UnDirected Graph.

    Implementation Details:
    Graph are stored as a dictionary with key as the name of the node, and value
    as dict containing node attributes and the adjacency list to store edges
    with the weights.

    Here is a sample example for graph A --(0.3)--> B:
    {

        "A": { "attr": {} , "adjacent_nodes" : [
                    { "B" : 0.3 } // keyname for connected node and weight
                ]
            },
        "B": { "attr": {}, "adjacent_nodes" : [] }
    }

    Note: "attr" holds attributes / data specific to nodes.

    Since the number of connections are stored in the array, to check whether
    Node say A is connected to node B, we will have to traverse the list in
    the worst case. Therefore, if the number of connections are say "e", then linear
    search in list will be O(e). This can be improved to O(log(e)) if any sorting
    order can be assumed and maintained in the list using binary search.

    This approach is better than adjacency matrix in most cases (except when
    all nodes are connected to every other node) because we don't need
    to store the data for all the other nodes in the list .

    Check here for more info: https://www.youtube.com/watch?v=k1wraWzqtvQ
    """

    # key to store node attributes
    _ATTR = "_attr"

    # key to store adjacency list
    _ADJACENT_NODES = "_adjacent_nodes"

    def __init__(self):
        """
        Initialize the graph
        """

        # graph
        self.graph = {}

        # has loops
        self.graph_has_loops = False

    def add_node(self, key: str, attr: dict = None):
        """
        Add a node given its key and the attributes.

        :param key: The unique key for the graph
        :type key: str
        :param attr: Attributes of the node
        :type attr:
        :return:
        :rtype:
        """

        if key not in self.graph.keys():
            self.graph[key] = {
                self._ATTR: attr if attr is not None else {},
                self._ADJACENT_NODES: []
            }
        else:
            raise DuplicateNodeNotAllowed(key)

    def get_all_nodes(self):
        """
        Get all the nodes of the graph.

        :return: the key for all the nodes
        :rtype: list
        """

        return list(self.graph.keys())

    def get_node(self, key: str):
        """
        Retrieve the node given its key.
        :param key: unique key name of the node
        :type key: str
        :return: node data
        :rtype: dict
        """

        if key in self.graph.keys():
            return self.graph[key]
        else:
            raise NodeDoesNotExist(key)

    def get_weight_of_edge(self, node, adjacent_node):
        """
        Get weight of edge connecting node and adjacent node.

        :param node: the source node name
        :type node: str
        :param adjacent_node: the adjacent node name
        :type adjacent_node: str
        :return: weight of the edge
        :rtype: float
        """
        adjacent_nodes = self.find_adjacent_nodes(node, only_keys=False)

        data = list(filter(lambda n: list(n.keys())[0] == adjacent_node, adjacent_nodes))

        if data:
            return data[0][adjacent_node]
        else:
            raise AdjacentNodeDoesNotExist(node, adjacent_node)

    def set_attr(self, node: str, value: dict):
        """
        Set attribute of the node. The attribute value is a dict.

        :param node: the node name for which the attribute has to be set
        :type node: str
        :param value: dictionary containing the attributes
        :type node: dict
        :return:
        :rtype:
        """

        if node in list(self.graph.keys()):
            self.graph[node][self._ATTR] = value
        else:
            raise NodeDoesNotExist(node)

    def get_attr(self, node: str):
        """
        Gets the attribute of the node given its name.

        :param node: name of the node
        :type node: str
        :return: attributes dictionary of the node
        :rtype: dict
        """

        if node in list(self.graph.keys()):
            return self.graph[node][self._ATTR]
        else:
            raise NodeDoesNotExist(node)

    def as_dict(self):
        """
        Returns the graph in the form of the dictionary.

        :return: graph as dictionary
        :rtype: dict
        """

        return self.graph

    def add_edge(self, source: str, destination: str, weight: float = 0.0):
        """
        Connect two nodes given their name (key) and the weight.
        Use this method to connect two nodes of the same graph.

        :param source: name of the source node
        :type source: str
        :param destination: name of the destination node
        :type destination: str
        :param weight: weight of the edge
        :type weight: float
        :return:
        :rtype:
        """

        if source not in self.graph:
            raise NodeDoesNotExist(source)
        if destination not in self.graph:
            raise NodeDoesNotExist(destination)

        # add node2 as a connection in node 1
        self.graph[source][self._ADJACENT_NODES].append(
            {destination: weight}
        )

    def connect_graph(self, destination: Graph, using_node: str, to_node: str, weight: float = 0.0):
        """
        Connect two nodes given their key and the weight.
        Use this method to connect two nodes of different graph.
        Post this operation the two graphs will loose their individual state and be treated as one,
        so both the source and destination graph will be the same.

        :param destination: destination graph to connect with
        :type destination: Graph
        :param using_node: which node (key) to use when connecting from source
        :type using_node: str
        :param to_node:which node (key) to use when connecting to destination
        :type to_node: str
        :param weight: weight of the edge, default to 0.0
        :type weight: float
        :return:
        :rtype:
        """

        destination_graph = destination.as_dict()
        self.graph.update(**destination_graph)

        # connect the nodes
        self.add_edge(using_node, to_node, weight)

    def find_adjacent_nodes(self, key: str, only_keys: bool = True):
        """
        Returns the list of adjacent node for the given node.

        :param key: node for which adjacent nodes needs to be retrieved
        :type key: str
        :param only_keys: Whether to retrieve only key names or weight data as well (default to True)
        :type only_keys: bool
        :return: list of adjacent graph nodes
        :rtype: list
        """
        # returns list of nodes adjacent to current node

        if key not in list(self.graph.keys()):
            raise NodeDoesNotExist(key)

        if not only_keys:
            return list(self.graph[key][self._ADJACENT_NODES])
        else:
            return list(map(lambda node: list(node.keys())[0], self.graph[key][self._ADJACENT_NODES]))

    def get_total_edges(self):
        """
        Calculates the total number of edges in the graph. For Directed graph, the sum of all adjacent edges for
        all the nodes gives the total number of edges.
        :return: total number of edges in the graph
        :rtype: int
        """
        edges = 0
        for vertex in self.get_all_nodes():
            edges += len(self.graph[vertex][self._ADJACENT_NODES])

        return edges

    def walk_dfs_recursive(self, node: str, visited_nodes: list, callback=None):
        """
        This is recursive implementation of DFS. There is no need to maintain
        a separate stack here because recursion itself brings the stack behaviour
        when calling itself repeatedly on adjacent nodes.

        Runtime: O(|V| + |E|) [For explanation look at iterative method]

        Here via recursion every vertex is visited, and each time we evaluate the adjacent
        nodes (via adjaceny list) which when ran for every node is equal to |E|. Since we
        also do some constant time operations like adding visited node to a list, and do that
        for |V| times, the overall runtime is O(|V| + |E|).

        NOTE THE SIMPLE IMPLEMENTATION OF RECURSION OVER ITERATIVE METHOD.

        :param node: the node that is visited
        :type node: str
        :param visited_nodes: list of already visited nodes
        :type visited_nodes: list
        :param callback: callback method to run when node is visited
        :type callback: function
        :return:
        :rtype:
        """

        # run some method over the node
        if callback is not None:
            callback(node)

        # mark the node as visited
        visited_nodes.append(node)

        # get the adjacent nodes
        adjacent_nodes = self.find_adjacent_nodes(node)

        # recurse with the adjacent node if it has not been visited
        for node in adjacent_nodes:
            if node not in visited_nodes:
                self.walk_dfs_recursive(node, visited_nodes, callback)

    def walk_dfs_iterative(self, start_node: str, callback=None):
        """
        Walk the graph in BFS manner.

        The time complexity of this algorithm is O(|V| + |E|) where
        |V| = number of vertices
        |E| = number of edges

        The pseudocode for dfs is:

        while stack is not empty:                   O(|V|) - total number of vertices
            pop node from stack                     O(1) - removing last element
            find adjacent nodes to the node         O(|Eadj|) - length of adjacent list for node
            add to the stack if not traversed       O(1) - add to stack


        Runtime =  |v| ( O(1) + O(|Eadj|) + O(1) )
                =  2 O(|v|) + O(|Eadj| *  |V|)


        For a graph, the traversing adjacent for each node is equal to the total number of edges.
        Therefore,  O(|Eadj| *  |V|) = O(|E|).

        Runtime = 2 O(|v|) + O(|E|)

        Since, we ignore the constant in asymptotic behavior, runtime is: O(|V| + |E|)

        If the graph is dense (every node connected to all other), the number of nodes
        in the adjacent list = |V| - 1, and the adjacency list is traversed for each node,
        therefore

        runtime = O(|V|) + O(|V|) + O(|V| * (|V| - 1))
                = 2 O(|V|) + O(|V|^2)
                ~ O(|V|^2)

        Note:  O(|V|^2) >>>> O(|V| + |E|)


        :param start_node: The start node key name for traversal
        :type start_node: str
        :param callback: If provided, the callback function will be executed for every node
        :type callback: function
        :return:
        :rtype:
        """
        # stack to maintain the nodes which have to be visited
        visit_nodes = [start_node]

        # keep track of explored nodes
        explored_nodes = []

        # while stack is not empty
        while len(visit_nodes) > 0:

            # get the last node from the stack (to imply it has been visited)
            node = visit_nodes.pop()

            # run the callback
            if callback is not None:
                callback(node)

            # get the adjacent nodes
            adjacent_nodes = self.find_adjacent_nodes(node)

            # mark the adjacent nodes as explored if not already
            # and add them to the visit_nodes
            for an in adjacent_nodes:

                # if node has not already been explored
                if an not in explored_nodes:
                    explored_nodes.append(an)
                    visit_nodes.append(an)

    def walk_bfs_recursive(self, visit_nodes: list, explored_nodes: list, callback=None):
        """

        Recursive BFS is similar to the iterative method, and the recursion is just
        iterating through the nodes maintained in the queue which is passed along
        whereas the stack is inherently available while recursing in DFS.

        This makes DFS implementation simple and memory efficient.

        Runtime: O(|V| + |E|) [For explanation look at iterative method]

        Here via recursion every vertex is visited, and each time we evaluate the adjacent
        nodes (via adjaceny list) which when ran for every node is equal to |E|. Since we
        also do some constant time operations like adding visited node to a list, and do that
        for |V| times, the overall runtime is O(|V| + |E|).

        :param visit_nodes: nodes to be visited in the iteration
        :type visit_nodes: list
        :param explored_nodes: nodes which have been explored in the current iteration
        :type explored_nodes: list
        :param callback: callback method to run when traversing node
        :type callback: function
        :return:
        :rtype:
        """

        if len(visit_nodes) > 0:

            # get the node from the queue
            node = visit_nodes.pop(0)

            # run some method over the node
            if callback is not None:
                callback(node)

            # get the adjacent nodes
            adjacent_nodes = self.find_adjacent_nodes(node)

            # if adjacent node is not visited, add it to the queue
            for an in adjacent_nodes:
                if an not in explored_nodes:
                    explored_nodes.append(an)
                    visit_nodes.append(an)

            self.walk_bfs_recursive(visit_nodes, explored_nodes, callback)

    def walk_bfs_iterative(self, start_node: str, callback=None):
        """
        Walk the graph in BFS manner.

        Use a queue to maintain the node to be traversed. The only difference between this
        and BFS is how the next node is picked up from the list - here it is a queue
        so the first item is picked up while in BFS it was a stack and the last
        item is picked.

        The time complexity of this algorithm is O(|V| + |E|) where
        |V| = number of vertices
        |E| = number of edges

        The pseudocode for bfs is:

        while queue is not empty:                   O(|V|) - total number of vertices
            pop first node from queue               O(1) - removing last element
            find adjacent nodes to the node         O(|Eadj|) - length of adjacent list for node
            add to the queue if not traversed       O(1) - add to stack


        Runtime =  |v| ( O(1) + O(|Eadj|) + O(1) )
                =  2 O(|v|) + O(|Eadj| *  |V|)


        For a graph, the traversing adjacent for each node is equal to the total number of edges.
        Therefore,  O(|Eadj| *  |V|) = O(|E|).

        Runtime = 2 O(|v|) + O(|E|)

        Since, we ignore the constant in asymptotic behavior, runtime is: O(|V| + |E|)

        If the graph is dense (every node connected to all other), the number of nodes
        in the adjacent list = |V| - 1, and the adjacency list is traversed for each node,
        therefore

        runtime = O(|V|) + O(|V|) + O(|V| * (|V| - 1))
                = 2 O(|V|) + O(|V|^2)
                ~ O(|V|^2)

        Note:  O(|V|^2) >>>> O(|V| + |E|)

        :param start_node: The start node key name for traversal
        :type start_node: str
        :param callback: If provided, the callback function will be executed for every node
        :type callback: function
        :return:
        :rtype:
        """

        # queue to maintain the nodes which have to be visited
        visit_nodes = [start_node]

        # keep track of explored nodes
        explored_nodes = []

        # while stack is not empty
        while len(visit_nodes) > 0:

            # get the first node from the queue (to imply it has been visited)
            node = visit_nodes.pop(0)

            # run the callback
            if callback is not None:
                callback(node)

            # get the adjacent nodes
            adjacent_nodes = self.find_adjacent_nodes(node)

            # mark the adjacent nodes as explored if not already
            # and add them to the visit_nodes
            for an in adjacent_nodes:

                # if node has not already been explored
                if an not in explored_nodes:
                    explored_nodes.append(an)
                    visit_nodes.append(an)

    def _dfs_modified_find_path_between_nodes(self, node: str, end: str,
                                              paths: list, path_stack: list):
        """
        This is a modified DFS implementation which will use a path_stack to hold the traversed
        path to a node, and end it to the paths list when it reaches the end.

        Note: The method does not maintain visited nodes because this is not basic DFS where
        a node has to be traversed only once.

        Algorithm Details:

        The basic idea behind the algorithm is to add a node to path_stack as it is traversed. This
        stack contains the path to the end node once it reached there. Also, when the recursion
        backtracks (or return), we pop out last node from the path_stack array to indicate that
        and then follow along the new traversal path.

        Running Time: O(|V| * |V|)

        For worst case scenarios each node will be connected to every other node.

        :param node: node name which is visited
        :type node: str
        :param end: node name of destination node
        :type end: str
        :param paths: list containing all the paths to destination
        :type paths: list
        :param path_stack: stack to maintain a single path
        :type path_stack: list
        :return:
        :rtype:
        """

        # add in current path path
        path_stack.append(node)

        # if we reach the end node, path_stack will contain the path
        # so append it to the paths list
        if node == end:

            # create new list from stack
            path_to_add = [*path_stack]

            # add the path stack as we have reached the end
            paths.append(path_to_add)
        else:

            # find the adjacent nodes, and recurse
            adjacent_nodes = self.find_adjacent_nodes(node)
            for ad_n in adjacent_nodes:

                self._dfs_modified_find_path_between_nodes(ad_n, end, paths, path_stack)

                # here we have retraced back from recursion stack
                # so pop item from current path
                path_stack.pop()

    def get_all_paths_to_node(self, node: str, from_node: str):
        """
        Get all paths to a node in the graph given the starting node.
        This will include shortest path as well as longest paths, and everything in between.

        Note: THIS DOES NOT WORK FOR UNDIRECTED GRAPH AS THERE CAN BE INFINITE NUMBER OF PATHS.

        Algorithm details:
        We use a modified version of DFS (_dfs_modified_find_path_between_nodes)
        in which we pass a list to store all paths. The dfs_modified method will
        evaluate all the paths and add it to that list.
        This list is then returned back as result.

        :param node: The node to which the path needs to be evaluated
        :type node: str
        :param from_node: The starting node to trace teh path
        :type from_node: str
        :return: list of strings (each depicting comma separated nodes) to all paths
        :rtype: list
        """

        # contains all paths to destination from source
        paths = []

        # add all paths to the paths list
        self._dfs_modified_find_path_between_nodes(from_node, node, paths, [])

        # convert list of list to list of strings (comma separated)
        paths = list(map(lambda path: ", ".join(path), paths))

        return paths

    def _dfs_modified_find_loop(self, node: str, stack: list, has_loop: list):
        """

        DFS to traverse the graph to find the loop and collect the nodes forming
        the loop in a stack.

        :param node: node name of currently visited node
        :type node: str
        :param stack: stack to maintain the nodes forming the loop
        :type stack: list
        :param has_loop: Boolean to maintain if loop has been detected.
        :type has_loop: bool
        :return:
        :rtype:
        """
        # if node is in the stack
        if node in stack:
            has_loop[0] = True

            # find the index in stack where it was previously added
            previous_node_index = stack.index(node)
            for i in range(previous_node_index):
                stack.pop(0)
        else:
            stack.append(node)

            # find adjacent nodes
            adjacent_nodes = self.find_adjacent_nodes(node)
            for ad_n in adjacent_nodes:
                # recurse
                self._dfs_modified_find_loop(ad_n, stack, has_loop)

                # break if loop is detected
                if has_loop[0]:

                    # stack has the loop nodes, so we break
                    break
                else:
                    # removing last node when retracing back
                    stack.pop()

    def has_loop(self):
        """
        Check if graph has loops.

        Algorithm Details:
        Following are the steps
        1. Get all nodes of the graph
        2. iterate through each node
            1. traverse the graph using DFS, and pass mutable list to track the loop
            2. If loop is found
                break the iteration and return True
            3 else:
                continue with next node as starting point
        3. After traversing the graph using each node as starting point, if no loop is detected,
        the graph does not have loop

        Runtime: O (|V| * |V|)

        :return: True / False if graph has loop, and the nodes which form the loop
        :rtype: tuple
        """

        # assume no loops exist
        loop_found = False
        loop = []

        # iterate through all nodes
        for node_key in list(self.graph.keys()):
            has_loop = [False]
            stack = []

            # traverse the graph from node
            self._dfs_modified_find_loop(node_key, stack, has_loop)

            # if loop detected, set loop_found and break
            if has_loop[0]:
                loop_found = True
                loop = stack
                break

        return loop_found, loop

    def relaxation(self, node: str, visited: list, attr_name: str, max_number: float):
        """

        Relaxation of node is a process of adjusting the cost / distance of its adjacent nodes such that
        cost / distance is minimized when traversing from source.

        :param node: the node to relax.
        :type node: str
        :param visited: list of visited nodes
        :type visited: list
        :param attr_name: the name of custom attribute of node which has cost data
        :type attr_name: str
        :param max_number: the max distance between two nodes if not connected
        :type max_number: float
        :return:
        :rtype:
        """
        adjacent_nodes = self.find_adjacent_nodes(node)

        # attributes for node
        node_attribute_data = self.get_attr(node)

        for ad_n in adjacent_nodes:
            adjacent_node_attribute_data = self.get_attr(ad_n)
            weight_node_to_ad_n = self.get_weight_of_edge(node, ad_n)
            if adjacent_node_attribute_data[attr_name] > node_attribute_data[attr_name] + weight_node_to_ad_n:
                adjacent_node_attribute_data[attr_name] = node_attribute_data[attr_name] + weight_node_to_ad_n

        # mark the node visited
        visited.append(node)

        # find the smallest that has not been visited
        attributes_map = list(map(lambda node_key: (node_key, self.graph[node_key][self._ATTR][attr_name]),
                             [key for key in list(self.graph.keys()) if key not in visited]))

        # if we have nodes that are not visited
        if len(attributes_map):

            sorted_nodes = sorted(attributes_map, key=lambda node_data: node_data[1])
            smallest_node_key = sorted_nodes[0][0]

            # call relaxation on that node
            self.relaxation(smallest_node_key, visited, attr_name, max_number)

    def run_dijikstra(self, start_node: str = None):
        """
        Run dijikstra algorithm given its starting (source) node.

        :param start_node: The source node name
        :type start_node: str
        :return: dictionary containing shortest path from source to all nodes in graph
        :rtype: dict
        """

        _attr_name = "distance"
        _MAX_INT = float(sys.maxsize)

        # visited nodes
        visited = []

        # all nodes
        all_nodes = list(self.graph.keys())

        # pick any node from the graph

        if start_node is None:
            node = all_nodes[0]
        else:
            node = start_node

        # set attribute (distance) of the node to 0.0
        self.set_attr(node, {_attr_name: 0.0})

        # for all other nodes set a highest value
        for n in all_nodes:
            if n != node:
                self.set_attr(n, {_attr_name: _MAX_INT})

        # relax the node recursively till all nodes are visited
        self.relaxation(node, visited, _attr_name, _MAX_INT)

        shortest_distance_data = {}
        for node_key in list(self.graph.keys()):
            shortest_distance_data[node_key] = self.graph[node_key][self._ATTR][_attr_name]

        return shortest_distance_data


class UnDirectedGraph(DirectedGraph):
    """
    For ease of implementation, we use DirectedGraph as a base for UndirectedGraph, and
    for every edge added between source node -> destination node, another edge will
    be added between destination node -> source node. This allows to use most of the implementation
    from Directed Graph without big modifications.

    The trade-off with this approach is that we duplicate edge information with the graph but we
    gain on the extra computation required to assume that relation.

    The graph will be stored the same way as DirectedGraph.
    """

    def __init__(self):
        super(UnDirectedGraph, self).__init__()
        self.disjoint_set_api = DisjointSetAPI()

    def add_edge(self, source: str, destination: str, weight: float = 0.0):
        """
        Connect two nodes given their name (key) and the weight.
        Use this method to connect two nodes of the same graph.
        In Undirected graph add another edge between destination to source
        in addition to adding an edge from source to destination

        :param source: name of the source node
        :type source: str
        :param destination: name of the destination node
        :type destination: str
        :param weight: weight of the edge
        :type weight: float
        :return:
        :rtype:
        """

        # add an edge from source to destination
        super(UnDirectedGraph, self).add_edge(source, destination, weight)

        # add an edge from destination to source
        self.graph[destination][self._ADJACENT_NODES].append(
            {source: weight}
        )

    def get_total_edges(self):
        """
        For Undirected graph an edge is counted twice (A -> B also means B -> A), so we divide the number of edges by 2.
        This also means the the count from Directed graph implementation will always be a multiple of 2.
        :return: total number of edges in the graph
        :rtype: int
        """
        edges_count = super(UnDirectedGraph, self).get_total_edges()
        return int(edges_count / 2)

    def _dfs_modified_find_loop(self, node: str, stack: list, has_loop: list):
        """
        Modified DFs to find the loop using disjoint sets. Once a loop is detected, the stack will contain
        the vertices / nodes forming the loop.

        :param node: node that is being visited
        :type node: str
        :param stack: collection of nodes forming loop
        :type stack: list
        :param has_loop: Whether the loop has been detected
        :type has_loop: list
        :return:
        :rtype:
        """

        stack.append(node)

        adjacent_nodes = self.find_adjacent_nodes(node, only_keys=True)
        for ad_n in adjacent_nodes:

            # check if adjacent node is not taking back to previous node
            # adding None so the condition can work smoothly
            if ad_n != [None, None, *stack][-2]:

                # check if nodes form disjoint set
                if self.disjoint_set_api.is_disjoint(node, ad_n):

                    # take a union of the set
                    self.disjoint_set_api.union(node, ad_n)

                    self._dfs_modified_find_loop(ad_n, stack, has_loop)

                    # when recurse back if loop has been detected, break
                    if has_loop[0]:
                        break
                else:
                    # loop will be created when adding node and ad_n (as a edge)

                    # get the previous index of the vertex
                    previous_index = stack.index(ad_n)

                    # remove all nodes before the index so we only have nodes
                    # forming the loop
                    for i in range(previous_index):
                        stack.pop(0)

                    # set loop to True
                    has_loop[0] = True
                    break

    def has_loop(self):
        """
        For undirected graphs disjoint sets are used to detect a cycle.
        :return: Whether graph has cycle and the nodes which form the cycle
        :rtype: True / False if graph has loop, and the nodes which form the loop
        """

        vertices = self.get_all_nodes()
        vertices_forming_loop = []
        has_loop = [False]

        self.disjoint_set_api.create(vertices)

        # start with the first vertex
        self._dfs_modified_find_loop(vertices[0], vertices_forming_loop, has_loop)

        return has_loop[0], vertices_forming_loop

    def _find_adjacent_node_with_min_cost(self, node: str, excluded_nodes: list = None):
        """
        Finds the adjacent node with minimum cost.
        Since the node can be connected to all the other nodes the running time is O(|V|).

        :param node: node to process
        :type node: str
        :param excluded_nodes: list of excluded nodes
        :type excluded_nodes: list
        :return:
        :rtype:
        """

        # holds the min cost
        min_size = sys.maxsize

        # adjacent node with min cost
        ad_n_with_min_cost = None

        adjacent_nodes = self.find_adjacent_nodes(node, only_keys=False)

        exclusions = [] if excluded_nodes is None else excluded_nodes

        # traverse through all adjacent nodes to find min cost edge
        for ad_n in adjacent_nodes:
            ad_n_key = list(ad_n.keys())[0]
            ad_n_cost = list(ad_n.values())[0]
            if ad_n_key not in exclusions:
                if ad_n_cost < min_size:
                    min_size = ad_n_cost
                    ad_n_with_min_cost = ad_n_key

        return ad_n_with_min_cost, min_size

    def _prims(self, spanning_tree, source_node, destination_node, cost_edge, total_cost):
        """
        Connects the edge to the spanning tree and evaluates the next edge to be connected
        using recursion.

        :param spanning_tree: Undirected graph as a spanning tree
        :type spanning_tree: UnDirectedGraph
        :param source_node: source node to connect the node
        :type source_node: str
        :param destination_node: destination node to connect the node
        :type destination_node: str
        :param cost_edge: cost of the edge getting connected in the spanning tree
        :type cost_edge: float
        :param total_cost: total cost of the spanning tree
        :type total_cost: list
        :return:
        :rtype:
        """
        print("Connecting edge %s->%s with cost %.1f" % (source_node, destination_node, cost_edge))

        # add the destination node, source node will already exist
        spanning_tree.add_node(destination_node)
        spanning_tree.add_edge(source_node, destination_node, weight=cost_edge)

        # add the cost
        total_cost[0] += cost_edge

        # check if the spanning tree property now holds
        if len(spanning_tree.get_all_nodes()) == len(self.get_all_nodes()) and \
                spanning_tree.get_total_edges() == len(self.get_all_nodes()) - 1:
            print("Spanning tree complete. Finishing ...")
        else:

            # parent node to which the next min is to be added
            parent_node = None

            # holds the node with min cost
            node_with_min_cost = None

            # min cost of node
            min_size = sys.maxsize

            spanning_tree_all_nodes = spanning_tree.get_all_nodes()

            # find the node with minimum cost adjacent to any node in the spanning tree
            for node in spanning_tree_all_nodes:
                resultant_node, size = self._find_adjacent_node_with_min_cost(node,
                                                                              excluded_nodes=spanning_tree_all_nodes)

                if resultant_node is not None:
                    if size < min_size:
                        node_with_min_cost = resultant_node
                        parent_node = node
                        min_size = size

            # if parent node and node with next min are calculated, recurse
            if parent_node is not None and node_with_min_cost is not None:
                self._prims(spanning_tree, parent_node, node_with_min_cost, min_size, total_cost)

    def _convert_graph_to_list(self):
        """
        Converts the graph to a list.

        :return:
        :rtype:
        """
        graph = []
        for node, node_data in self.graph.items():
            for ad_n in node_data[self._ADJACENT_NODES]:
                name_ad_n = list(ad_n.keys())[0]
                cost_n_to_ad_n = list(ad_n.values())[0]

                # only add if the node and edge has not been added before
                if [node, name_ad_n, cost_n_to_ad_n] not in graph and [name_ad_n, node, cost_n_to_ad_n] not in graph:
                    graph.append([node, name_ad_n, cost_n_to_ad_n])

        return graph

    @staticmethod
    def _get_edge_with_min_cost(graph: list):
        """

        :param graph:
        :type graph:
        :return:
        :rtype:
        """

        if len(graph) > 0:
            edge = graph.pop(0)
            return edge
        else:
            return []

    def generate_minimum_cost_spanning_tree_using_kruskal(self):
        """
        Generate minimum cost spanning tree using Kruskal's Algorithm.

        Pseudo code for Kruskal's algorithm is:
        1. Create a Graph say STG (Spanning Tree Graph - A subset of Graph) from this edge
        2. Add all the vertices of the graph in the disjoint set
        3. Find the edge with minimum cost / weight
        4. Check if the vertices connecting the edge forms a cycle
            4.1 If not - add the vertices to spanning tree (STG)
            4.2 If yes - ignore the edge
        5. go to step 2. [for remaining edges]

        :return:
        :rtype:
        """

        # get all the vertices
        vertices = self.get_all_nodes()

        # total vertices
        num_of_vertices_graph = len(vertices)

        # create a disjoint set
        disjoint_api = DisjointSetAPI()
        disjoint_api.create(vertices)

        # create a spanning tree
        spanning_tree = UnDirectedGraph()
        num_of_vertices_spanning = len(spanning_tree.get_all_nodes())

        # convert graph to a list
        sorted_graph = sorted(self._convert_graph_to_list(), key=lambda e: e[2])

        # total cost of the spanning tree
        total_cost = 0

        spanning_tree_complete = False


        # while spanning tree property is not attained
        while not spanning_tree_complete:

            # check if the spanning tree property now holds
            if len(spanning_tree.get_all_nodes()) == len(self.get_all_nodes()) and \
                    spanning_tree.get_total_edges() == len(self.get_all_nodes()) - 1:
                spanning_tree_complete = True
                print("Spanning tree complete. Finishing ...")
            else:
                edge = self._get_edge_with_min_cost(sorted_graph)
                if edge:

                    # check if the vertices of the edge forms a disjoint set or not
                    # add to spanning tree only if sets are disjoint
                    if disjoint_api.is_disjoint(edge[0], edge[1]):
                        print("Connecting edge %s->%s with cost %.1f" % (edge[0], edge[1], edge[2]))
                        if edge[0] not in spanning_tree.get_all_nodes():
                            spanning_tree.add_node(edge[0])

                        if edge[1] not in spanning_tree.get_all_nodes():
                            spanning_tree.add_node(edge[1])

                        # update the spanning tree
                        spanning_tree.add_edge(edge[0], edge[1], edge[2])
                        total_cost += edge[2]

                        # update the count of spanning tree vertices
                        num_of_vertices_spanning = len(spanning_tree.get_all_nodes())

                        # take union of disjoint set
                        disjoint_api.union(edge[0], edge[1])
                    else:
                        print("Edge %s->%s are not disjoint, and make a cycle. Ignoring it." %(edge[0], edge[1]))

        return {
            "tree": spanning_tree.as_dict(),
            "cost": total_cost
        }

    def generate_minimum_cost_spanning_tree_using_prims(self):
        """
        Generate minimum cost spanning tree using Prim's Algorithms.

        Pseudo code for Prim's algorithm is:
        1. Find edge with minimum cost / weight
        2. Create a Graph say STG (Spanning Tree Graph - A subset of Graph) from this edge
        3. Find the node which has the minimum cost but is also connected with the nodes in the STG in step 2.
        4. Check If no_of_nodes in STG = no_of_nodes in graph and no_of_edges in STG = no_of_nodes in graph - 1
            4.1 Exit
        5. Add the node to graph STG
        6. Move to step 3.

        At the end STG will be the minimum cost spanning tree.

        NOTE: Prim's algorithm does not work for disconnected graph as it always look for the adjacent nodes
        with minimum cost.
        Also Prim's does not work for directed graphs because there might be a directed graph which has no more adjacent
        nodes but still many of its nodes remain unvisited when constructing the spanning tree.

        Runtime:

        For each node in STG, the algorithm finds the node with minimum cost from their adjacent nodes. Iterating through
        the adjacent nodes for all the nodes in STG at max can take O(|E|) because we loop through all the edges
        in the original graph, and this process is repeated for each node in STG therefore runtime is:

        O(|V| * |E|)

        :return: dictionary containing spanning tree and the cost
        :rtype: dict
        """

        parent_node = None
        child_node = None

        # min cost
        min_cost = sys.maxsize

        # nodes which has been visited
        visited_nodes = []

        # find the edge with the minimum cost
        for node in self.get_all_nodes():
            visited_nodes.append(node)
            resultant_node, size = self._find_adjacent_node_with_min_cost(node, excluded_nodes=visited_nodes)

            if resultant_node is not None:
                if size < min_cost:
                    min_cost = size
                    parent_node = node
                    child_node = resultant_node

        spanning_tree = UnDirectedGraph()
        spanning_tree.add_node(parent_node)

        # total cost of the spanning tree
        total_cost = [0]

        self._prims(spanning_tree, parent_node, child_node, min_cost, total_cost)

        # return the spanning tree and cost
        return {
            "tree": spanning_tree.as_dict(),
            "cost": total_cost[0]
        }






