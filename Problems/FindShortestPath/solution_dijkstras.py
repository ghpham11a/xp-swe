import heapq
from collections import defaultdict

class UndirectedWeightedGraph(object):

    def __init__(self, size):
        self.size = size
        self.adjacency_list = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

def dijkstras(graph, src_node):

    prev_nodes = [None] * graph.size
    distances = [float("inf")] * graph.size
    pq = []

    distances[src_node] = 0

    for node in range(graph.size):
        heapq.heappush(pq, (distances[node], src_node))

    while pq:
        src_distance, src = heapq.heappop(pq)

        for dst, to_dst_weight in graph.adjacency_list[src]:
            new_weight = distances[src] + to_dst_weight

            if new_weight < distances[dst]:
                prev_nodes[dst] = src
                distances[dst] = new_weight
                heapq.heappush(pq, (new_weight, dst))

    return (distances, prev_nodes)

def find_shortest_path(graph, src_node, dst_node):
    distances, prev_nodes = dijkstras(graph, src_node)
    output = []

    if distances[dst_node] == float("inf"):
        return []

    curr_node = dst_node
    while curr_node != None:
        output.append(curr_node)
        curr_node = prev_nodes[curr_node]

    return output[::-1]

graph = UndirectedWeightedGraph(7)

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