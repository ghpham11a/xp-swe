import heapq

class UndirectedWeightedGraph(object):
    def __init__(self, size):
        self.size = size
        # Create an adjacency list where each index holds a list of (neighbor, weight) tuples.
        self.adjacency_list = [[] for _ in range(size)]

    def add_edge(self, u, v, weight):
        # Since the graph is undirected, add the edge in both directions.
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

def dijkstras(graph, src_node):
    # Initialize a list to track whether a node's shortest distance is finalized.
    visited = [False] * graph.size
    # Keep track of previous nodes to reconstruct the shortest paths if needed.
    prev_nodes = [None] * graph.size
    # Initialize distances from the source to every node as infinity.
    distances = [float("inf")] * graph.size

    # Priority queue (min-heap) to always pick the node with the smallest known distance.
    pq = []
    distances[src_node] = 0
    heapq.heappush(pq, (distances[src_node], src_node))

    # Process nodes until the queue is empty.
    while pq:
        # Extract the node with the smallest distance.
        src_distance, src = heapq.heappop(pq)
        # Mark this node as visited, meaning its shortest path is finalized.
        visited[src] = True

        # Iterate over each neighbor of the current node.
        for dst, to_dst_weight in graph.adjacency_list[src]:
            # If we've already finalized the shortest path for 'dst', skip it.
            if visited[dst]:
                continue

            # Calculate new potential distance to the neighbor.
            new_weight = distances[src] + to_dst_weight

            # If the new distance is smaller, update the distance and record the predecessor.
            if new_weight < distances[dst]:
                prev_nodes[dst] = src
                distances[dst] = new_weight
                # Push the neighbor with the updated distance into the priority queue.
                heapq.heappush(pq, (new_weight, dst))

    # Return the final shortest distances and the list of previous nodes for path reconstruction.
    return (distances, prev_nodes)


graph = UndirectedWeightedGraph(7)

graph.add_edge(0,1,2)
graph.add_edge(0,2,6)
graph.add_edge(1,3,5)
graph.add_edge(2,3,8)
graph.add_edge(3,4,10)
graph.add_edge(3,5,15)
graph.add_edge(4,6,2)
graph.add_edge(5,6,6)

assert(dijkstras(graph, 1) == ([2, 0, 8, 5, 15, 20, 17], [1, None, 0, 1, 3, 3, 4]))

print("PASS")