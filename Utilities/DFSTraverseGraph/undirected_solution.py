# Undirected Graph example
class UndirectedGraph:
    def __init__(self, size):
        self.size = size
        self.adjacency_list = [[] for _ in range(size)]
    
    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

def function(graph, node):

    output = []
    visited = [False] * graph.size

    dfs(graph, 0, output, visited)

    return output

def dfs(graph, node, output, visited):

    output.append(node)
    visited[node] = True 

    for neighbor in graph.adjacency_list[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, output, visited)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph.adjacency_list[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

undirected = UndirectedGraph(5)
undirected.add_edge(0, 1)
undirected.add_edge(0, 2)
undirected.add_edge(1, 3)
undirected.add_edge(2, 4)
dfs(undirected, 0)
