from collections import deque

class UndirectedGraph(object):

    def __init__(self, size):
        self.size = size
        self.adjacency_list = [[] for _ in range(size)]

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

def bfs(graph, node):

    output = []
    visited = [False] * graph.size
    queue = deque()

    queue.appendleft(node)
    visited[node] = True

    while queue:

        curr_node = queue.pop()
        output.append(curr_node)

        for neighbor in graph.adjacency_list[node]:
            if visited[neighbor] == False:
                queue.appendleft(neighbor)
                visited[neighbor] = True

    return output


graph = UndirectedGraph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

assert(bfs(graph, 2) == [2,0,1,3])

print("PASS")