from collections import deque

class DirectedAcyclicGraph(object):

    def __init__(self, size):
        self.adjacency_list = [[] for _ in range(size)]
        self.size = size

    def add_edge(self, src, dst):
        self.adjacency_list[src].append(dst)

    class CycleError(Exception):

        def __init__(self, message, errors):
            super().__init__(message)

def kahns(graph):

    in_degrees = [0 for _ in range(graph.size)]

    for node in range(graph.size):
        for neighbor in graph.adjacency_list[node]:
            in_degrees[neighbor] += 1

    queue = deque()

    for node in range(graph.size):
        if in_degrees[node] == 0:
            queue.appendleft(node)

    output = []

    while queue:
        node = queue.pop()
        output.append(node)

        for neighbor in graph.adjacency_list[node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.appendleft(neighbor)

    return output

graph = DirectedAcyclicGraph(14)

graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(0, 6)
graph.add_edge(1, 4)
graph.add_edge(2, 6)
graph.add_edge(3, 1)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(4, 8)
graph.add_edge(6, 7)
graph.add_edge(6, 11)
graph.add_edge(7, 4)
graph.add_edge(7, 12)
graph.add_edge(9, 2)
graph.add_edge(9, 10)
graph.add_edge(10, 6)
graph.add_edge(11, 12)
graph.add_edge(12, 8)

assert(kahns(graph) == [0, 9, 13, 3, 2, 10, 1, 6, 7, 11, 4, 12, 5, 8])

print("PASS")

    