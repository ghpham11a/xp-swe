import heapq

class UndirectedWeightedGraph(object):

    def __init__(self, size):
        self.size = size
        self.adjacency_list = [[] for _ in range(size)]

    def add_edge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

def prims(graph):
    # The number of edges in a spanning tree is (number of vertices - 1).
    target_edge_count = graph.size - 1
    # Counter for how many edges are added to the MST.
    edge_count = 0         
     
    # Total cost (weight) of the MST.
    mst_cost = 0
     # To store the edges included in the MST.             
    mst_edges = [None] * target_edge_count

    # Keep track of vertices already included in the MST.
    visited = [False] * graph.size

    # Priority queue (min-heap) for edges based on weight.
    # Each entry in the heap is a tuple (edge weight, source vertex, destination vertex).
    pq = []

    # Start by adding all edges from vertex 0.
    prims_add_edges(graph, visited, pq, 0)

    # Continue until we either have all necessary MST edges or the priority queue is empty.
    while pq and edge_count != target_edge_count:
        # Pop the edge with the smallest weight.
        to_dst_weight, src, dst = heapq.heappop(pq)

        # If the destination vertex is already in the MST, skip it.
        if visited[dst]:
            continue

        # Add the edge to the MST.
        mst_edges[edge_count] = (src, dst, to_dst_weight)
        edge_count += 1
        mst_cost += to_dst_weight

        # Add new edges from the newly visited vertex.
        prims_add_edges(graph, visited, pq, dst)

    # If we haven't added enough edges, the graph might be disconnected.
    if edge_count != target_edge_count:
        return (None, None)

    return (mst_cost, mst_edges)

def prims_add_edges(graph, visited, pq, src):
    # Mark the current vertex as visited.
    visited[src] = True

    # Add all edges from the current vertex to the priority queue,
    # but only if the destination vertex has not been visited.
    for dst, to_dst_weight in graph.adjacency_list[src]:
        if not visited[dst]:
            heapq.heappush(pq, (to_dst_weight, src, dst))

graph = UndirectedWeightedGraph(10)
graph.add_edge(0, 1, 5)
graph.add_edge(1, 2, 4)
graph.add_edge(2, 9, 2)
graph.add_edge(0, 4, 1)
graph.add_edge(0, 3, 4)
graph.add_edge(1, 3, 2)
graph.add_edge(2, 7, 4)
graph.add_edge(2, 8, 1)
graph.add_edge(9, 8, 0)
graph.add_edge(4, 5, 1)
graph.add_edge(5, 6, 7)
graph.add_edge(6, 8, 4)
graph.add_edge(4, 3, 2)
graph.add_edge(5, 3, 5)
graph.add_edge(3, 6, 11)
graph.add_edge(6, 7, 1)
graph.add_edge(3, 7, 2)
graph.add_edge(7, 8, 6)

assert(prims(graph) == (14, [(0, 4, 1), (4, 5, 1), (4, 3, 2), (3, 1, 2), (3, 7, 2), (7, 6, 1), (1, 2, 4), (2, 8, 1), (8, 9, 0)]))


graph = UndirectedWeightedGraph(8)
graph.add_edge(0, 1, 10)
graph.add_edge(0, 2, 1)
graph.add_edge(0, 3, 4)
graph.add_edge(2, 1, 3)
graph.add_edge(2, 5, 8)
graph.add_edge(2, 3, 2)
graph.add_edge(2, 0, 1)
graph.add_edge(3, 2, 2)
graph.add_edge(3, 5, 2)
graph.add_edge(3, 6, 7)
graph.add_edge(3, 0, 4)
graph.add_edge(5, 2, 8)
graph.add_edge(5, 4, 1)
graph.add_edge(5, 7, 9)
graph.add_edge(5, 6, 6)
graph.add_edge(5, 3, 2)
graph.add_edge(4, 1, 0)
graph.add_edge(4, 5, 1)
graph.add_edge(4, 7, 8)
graph.add_edge(1, 0, 10)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 4, 0)
graph.add_edge(6, 3, 7)
graph.add_edge(6, 5, 6)
graph.add_edge(6, 7, 12)
graph.add_edge(7, 4, 8)
graph.add_edge(7, 5, 9)
graph.add_edge(7, 6, 12)

assert(prims(graph) == (20, [(0, 2, 1), (2, 3, 2), (3, 5, 2), (5, 4, 1), (4, 1, 0), (5, 6, 6), (4, 7, 8)]))

print("PASS")

