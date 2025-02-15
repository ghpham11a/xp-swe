import heapq

class UndirectedWeightedGraph(object):

    def __init__(self, size):
        self.size = size
        self.adjacency_list = [[] for _ in range(size)]

    def add_edge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

def dijkstras(graph, src_node):

    visited = [False] * graph.size
    prev_nodes = [None] * graph.size
    distances = [float("inf")] * graph.size

    pq = []
    distances[src_node] = 0
    heapq.heappush(pq, (distances[src_node], src_node))

    while pq:

        src_distance, src = heapq.heappop(pq)
        visited[src] = True

        for dst, to_dst_weight in graph.adjacency_list[src]:

            if visited[dst]:
                continue

            new_weight = distances[src] + to_dst_weight

            if new_weight < distances[dst]:
                prev_nodes[dst] = src
                distances[dst] = new_weight
                heapq.heappush(pq, (new_weight, dst))


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