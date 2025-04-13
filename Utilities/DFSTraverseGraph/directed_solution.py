class DirectedGraph:
    def __init__(self, size):
        self.size = size
        self.adjacency_list = [[] for _ in range(size)]
    
    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph.adjacency_list[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

directed = DirectedGraph(5)
directed.add_edge(0, 1)
directed.add_edge(0, 2)
directed.add_edge(1, 3)
directed.add_edge(2, 4)
dfs(directed, 0)

