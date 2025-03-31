class UndirectedGraph(object):
    def __init__(self, size):
        self.size = size
        # Each index contains a list of adjacent vertices.
        self.adjacency_list = [[] for _ in range(size)]

    def add_edge(self, u, v):
        # Even though a weight is provided, this graph is unweighted.
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

class Solution:
    
    def critical_connections(self, n, connections):

        graph = UndirectedGraph(n)
        for u, v in connections:
            graph.add_edge(u, v)

        articulation_points, bridges = self.modified_tarjans(graph)

        return list(map(list, bridges))
    
    def modified_tarjans(self, graph):

        # Initialize discovery times as -1 to denote unvisted notes
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
                self.tarjan_dfs(node, parent, disc, low, time, graph, articulation_points, bridges)

        return articulation_points, bridges
            
    def tarjan_dfs(self, node, parent, disc, low, time, graph, articulation_points, bridges):

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
                self.tarjan_dfs(neighbor, parent, disc, low, time, graph, articulation_points, bridges)

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

runner = Solution()

assert(runner.critical_connections(4, [[0,1],[1,2],[2,0],[1,3]]) == [[1,3]])

print("PASS")