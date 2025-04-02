class DirectedWeightedGraph(object):

    def __init__(self, size):
        self.size = size
        self.adjacency_list = [[] for _ in range(size)]

    def add_edge(self, rel_src, rel_dst, weight):
        self.adjacency_list[rel_src].append((rel_dst, weight))

def _bellman_ford(graph, start):

    distances = [float("inf") for _ in range(graph.size)]
    predecessor = [None for _ in range(graph.size)]

    graph_edges = []
    for rel_src, neighbors in enumerate(graph.adjacency_list):
        for rel_dst, rel_weight in neighbors:
            graph_edges.append((rel_src, rel_dst, rel_weight))

    for _ in range(graph.size - 1):
        for rel_src, rel_dst, rel_weight in graph_edges:
            if distances[rel_src] + rel_weight < distances[rel_dst]:
                distances[rel_dst] = distances[rel_src] + rel_weight
                predecessor[rel_dst] = rel_src


def bellman_ford(graph, start):

    # Step 1: Initialize distances from the start vertex to all other vertices.
    # All distances are set to "infinity" initially, except for the start vertex, which is 0.
    distances = [float("inf") for _ in range(graph.size)]
    # Predecessor array to record the path: which vertex precedes the current vertex in the shortest path.
    predecessor = [None for _ in range(graph.size)]
    distances[start] = 0

    # Step 2: Extract all edges from the graph.
    # This creates a list of edges in the format (source, destination, weight) for easy iteration.
    graph_edges = []
    for rel_src, neighbors in enumerate(graph.adjacency_list):
        for rel_dst, rel_weight in neighbors:
            graph_edges.append((rel_src, rel_dst, rel_weight))
    
    # Step 3: Relax all edges repeatedly.
    # We perform |V|-1 iterations, where |V| is the number of vertices.
    # In each iteration, update the distance if a shorter path is found.
    for _ in range(graph.size - 1):
        for rel_src, rel_dst, rel_weight in graph_edges:
            # Check if the current path from start -> rel_src -> rel_dst is shorter than the known distance.
            if distances[rel_src] + rel_weight < distances[rel_dst]:
                distances[rel_dst] = distances[rel_src] + rel_weight
                predecessor[rel_dst] = rel_src

    # Step 4: Check for negative weight cycles.
    # Perform extra iterations to propagate negative cycles.
    # If an edge can still be relaxed, then that vertex is affected by a negative cycle.
    for _ in range(graph.size - 1):
        for rel_src, rel_dst, rel_weight in graph_edges:
            if distances[rel_src] + rel_weight < distances[rel_dst]:
                # Mark the vertex as affected by a negative cycle.
                distances[rel_dst] = -float("inf")

    # Return the computed shortest distances and the predecessor information for each vertex.
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

