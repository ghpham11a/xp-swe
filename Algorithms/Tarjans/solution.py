from collections import defaultdict

class DirectedGraph(object):

    def __init__(self, size):
        self.size = size
        self.adjacency_list = [[] for i in range(size)]

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)

UNVISITED = -1

def tarjans(graph):

    time = [0]
    in_times = [UNVISITED] * graph.size
    low_links = [0] * graph.size
    on_stack = [False] * graph.size
    stack = []

    for node in range(graph.size):
        if in_times[node] == UNVISITED:
            tarjans_dfs(graph, time, in_times, low_links, on_stack, stack, node)

    return low_links

def tarjans_dfs(graph, time, in_times, low_links, on_stack, stack, node):
    stack.append(node)
    on_stack[node] = True
    time[0] += 1
    in_times[node] = low_links[node] = time[0]

    for neighbor in graph.adjacency_list[node]:
        if in_times[neighbor] == UNVISITED:
            tarjans_dfs(graph, time, in_times, low_links, on_stack, stack, neighbor)

        if on_stack[neighbor] == True:
            low_links[node] = min(low_links[node], low_links[neighbor])

    if in_times[node] == low_links[node]:
        while len(stack) > 0:
            stack_node = stack.pop()
            on_stack[stack_node] = False
            low_links[stack_node] = in_times[node]
            if stack_node == node:
                break


graph = DirectedGraph(8)

graph.add_edge(6, 0)
graph.add_edge(6, 2)
graph.add_edge(3, 4)
graph.add_edge(6, 4)
graph.add_edge(2, 0)
graph.add_edge(0, 1)
graph.add_edge(4, 5)
graph.add_edge(5, 6)
graph.add_edge(3, 7)
graph.add_edge(7, 5)
graph.add_edge(1, 2)
graph.add_edge(7, 3)
graph.add_edge(5, 0)

assert(tarjans(graph) == [1, 1, 1, 4, 5, 5, 5, 4])

print("PASS")