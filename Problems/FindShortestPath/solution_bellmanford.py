class DirectedWeightedGraph(object):

    def __init__(self, size):
        self.size = size
        self.adjacency_list = [[] for _ in range(size)]

    def add_edge(self, src, dst, weight):
        self.adjacency_list[src].append((dst, weight))
    
    def get_edges(self):
        graph_edges = []
        for src, neighbors in enumerate(graph.adjacency_list):
            for dst, to_dst_weight in neighbors:
                graph_edges.append((src, dst, to_dst_weight))
        return graph_edges

def bellman_ford(graph, start):

    distances = [float("inf") for _ in range(graph.size)]
    predecessor = [None for _ in range(graph.size)]

    distances[start] = 0

    graph_edges = graph.get_edges()
    
    for _ in range(graph.size - 1):
        for src, dst, to_dst_weight in graph_edges:
            if distances[src] + to_dst_weight < distances[dst]:
                distances[dst] = distances[src] + to_dst_weight
                predecessor[dst] = src

    for _ in range(graph.size - 1):
        for src, dst, to_dst_weight in graph_edges:
            if distances[src] + to_dst_weight < distances[dst]:
                distances[dst] = -float("inf")

    return distances, predecessor

def find_shortest_path(graph, start, end):

    output = []
    distances, predecessor = bellman_ford(graph, start)

    if distances[end] == float("inf"):
        return output

    node = end
    while predecessor[node] != None:
        if predecessor[node] == -1:
            return []
        output.append(node)
        node = predecessor[node]

    output.append(start)

    return output[::-1]

graph = DirectedWeightedGraph(7)

graph.add_edge(0,1,2)
graph.add_edge(0,2,6)
graph.add_edge(1,3,5)
graph.add_edge(2,3,8)
graph.add_edge(3,4,10)
graph.add_edge(3,5,15)
graph.add_edge(4,6,2)
graph.add_edge(5,6,6)

assert(find_shortest_path(graph, 1, 6) == [1, 3, 4, 6])
assert(find_shortest_path(graph, 0, 6) == [0, 1, 3, 4, 6])

print("PASS")