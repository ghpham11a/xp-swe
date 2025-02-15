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

graph = DirectedWeightedGraph(9)

graph.add_edge(0, 1, 1)
graph.add_edge(1, 2, 1)
graph.add_edge(2, 4, 1)
graph.add_edge(4, 3, -3)
graph.add_edge(3, 2, 1)
graph.add_edge(1, 5, 4)
graph.add_edge(1, 6, 4)
graph.add_edge(5, 6, 5)
graph.add_edge(6, 7, 4)
graph.add_edge(5, 7, 3)

test_output_distances = [0, 1, -float("inf"), -float("inf"), -float("inf"), 5, 5, 8, float("inf")]
test_output_predecessor = [None, 0, 3, 4, 2, 1, 1, 5, None]
assert(bellman_ford(graph, 0) == (test_output_distances, test_output_predecessor))


print("PASS")

