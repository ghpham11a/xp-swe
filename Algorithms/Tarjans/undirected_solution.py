class UndirectedGraph(object):
    def __init__(self, size):
        self.size = size
        # Each index contains a list of adjacent vertices.
        self.adjacency_list = [[] for _ in range(size)]

    def add_edge(self, u, v):
        # Even though a weight is provided, this graph is unweighted.
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

def modified_tarjans(graph):
    """
    Finds and returns all articulation points and bridges in an undirected graph.
    
    Parameters:
    - graph: an instance of UndirectedGraph.
    
    Returns:
    - articulation_points: a set of vertices that are articulation points.
    - bridges: a set of tuples (u, v) representing bridges.
    """
     
    # Initialize discovery times as -1 to denote unvisted notes
    # Essential for both marking visitation and serving as a reference point for the key comparisons that identify critical vertices and edges in the graph.
    disc = [-1] * graph.size 
    # Initialize low values 
    low = [-1] * graph.size 
    # To record DFS tree parents 
    parent = [None] * graph.size 

    articulation_points = set()
    bridges = set()
    time = [0]

    for node in range(graph.size):
        if disc[node] == -1:
            tarjan_dfs(node, parent, disc, low, time, graph, articulation_points, bridges)

    return articulation_points, bridges

def tarjan_dfs(node, parent, disc, low, time, graph, articulation_points, bridges):
    """
    Perform a DFS starting at vertex u, updating discovery and low-link times.
    Also, identify articulation points and bridges in the process.
    
    Parameters:
    - u: current vertex.
    - parent: list holding the parent of each vertex in the DFS tree.
    - disc: list holding discovery times for each vertex.
    - low: list holding the lowest discovery time reachable from each vertex.
    - time: a single-element list used as a mutable counter for discovery time.
    - graph: an instance of UndirectedGraph.
    - articulation_points: set to store identified articulation points.
    - bridges: set to store identified bridges (as (u, v) tuples).
    """
    
    # Set the discovery time and low value for current node
    disc[node] = low[node] = time[0]
    time[0] += 1
    child_count = 0

    # Iterate over all adjacent vertices of node
    for neighbor in graph.adjacency_list[node]:
        if disc[neighbor] == -1:
            child_count += 1
            # Set node(u) as parent of neighbor(v)
            parent[neighbor] = node
            tarjan_dfs(neighbor, parent, disc, low, time, graph, articulation_points, bridges)

            # Update low-link value for u based on child v
            low[node] = min(low[node], low[neighbor])

            # If u is root of DFS and has more than one child, it's an articulation point.
            if parent[node] is None and child_count > 1:
                articulation_points.add(node)

            # If node(u) is not root and low value of one child is at least node(u)'s discovery time,
            # then u is an articulation point.
            if parent[node] is not None and low[neighbor] >= disc[node]:
                articulation_points.add(node)

            # If the low-link value of neighbor(v) is greater than the discovery time of node(u)
            # then edge (u, v) is bridge.
            if low[neighbor] > disc[node]:
                bridges.add((node, neighbor))
        # neighbor(v) is visited and is not the parent of u (back edge).
        elif neighbor != parent[node]:
            low[node] = min(low[node], disc[neighbor])

graph = UndirectedGraph(7)

# Add edges to form a cycle: 0-1-2-0
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 0)

# Add additional edges to create a tree branch from the cycle:
# 1-3, and then a branch 3-4 and 3-5, with 5-6 forming a leaf branch.
graph.add_edge(1, 3)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(5, 6)

assert(modified_tarjans(graph) == ({1, 3, 5}, {(5, 6), (1, 3), (3, 4), (3, 5)}))

print("PASS")
