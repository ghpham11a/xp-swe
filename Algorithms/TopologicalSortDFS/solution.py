from enum import Enum

class DirectedAcyclicGraph(object):

    def __init__(self, size):
        self.adjacency_list = [[] for _ in range(size)]
        self.size = size

    def add_edge(self, src, dst):
        self.adjacency_list[src].append(dst)

    class CycleError(Exception):

        def __init__(self, message, errors):
            super().__init__(message)
 
class Marker(Enum):
    UNMARKED = 1
    TEMPORARY = 2
    PERMANENT = 3

def topological_sort(graph):
    markers = [Marker.UNMARKED] * graph.size
    output = [] 

    for node in range(graph.size):
        if node not in markers:
            topological_sort_dfs(node, graph, output, markers)

    return output[::-1]

def topological_sort_dfs(node, graph, output, markers):

    if markers[node] == Marker.PERMANENT:
        return

    if markers[node] == Marker.TEMPORARY:
        raise DirectedAcyclicGraph.CycleError("Cycle error detected", OSError())

    markers[node] = Marker.TEMPORARY

    for neighbor in graph.adjacency_list[node]:
        topological_sort_dfs(neighbor, graph, output, markers)

    markers[node] = Marker.PERMANENT
    output.append(node)


graph = DirectedAcyclicGraph(7)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(0,5)
graph.add_edge(1,3)
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(2,4)
graph.add_edge(3,4)
graph.add_edge(5,4)

assert(topological_sort(graph) == [6, 0, 5, 1, 2, 3, 4])

print("PASS")

