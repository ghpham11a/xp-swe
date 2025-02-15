class DirectedGraph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.num_edges = 0
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, src, dst):
        self.num_edges += 1
        self.adjacency_list[src].append(dst)

def graph_has_eulerian_path(graph):

    in_degrees = [0] * graph.num_vertices
    out_degrees = [0] * graph.num_vertices

    for src in range(graph.num_vertices):
        for dst in graph.adjacency_list[src]:
            out_degrees[src] += 1
            in_degrees[dst] += 1

    start_nodes, end_nodes = 0, 0

    for i in range(graph.num_vertices):
        if (out_degrees[i] - in_degrees[i]) > 1 or (in_degrees[i] - out_degrees[i]) > 1:
            return False
        elif out_degrees[i] - in_degrees[i] == 1:
            start_nodes += 1
        elif in_degrees[i] - out_degrees[i] == 1:
            end_nodes += 1

    return (end_nodes == 0 and start_nodes == 0) or (end_nodes == 1 and start_nodes == 1)

def find_start_node(graph):

    in_degrees = [0] * graph.num_vertices
    out_degrees = [0] * graph.num_vertices

    start = 0

    for src in range(graph.num_vertices):
        for dst in graph.adjacency_list[src]:
            out_degrees[src] += 1
            in_degrees[dst] += 1

    for i in range(graph.num_vertices):
        if out_degrees[i] - in_degrees[i] == 1:
            return i

        if out_degrees[i] > 0:
            start = i 

    return start

def find_eulerian_path(graph):
    output = []

    if not graph_has_eulerian_path(graph):
        return output

    find_eulerian_path_dfs(graph, output, find_start_node(graph))

    return output[::-1] if len(output) == graph.num_edges + 1 else []

def find_eulerian_path_dfs(graph, output, node):
    neighbors = graph.adjacency_list[node]

    while neighbors:
        dst = neighbors.pop()
        find_eulerian_path_dfs(graph, output, dst)

    output.append(node)

graph = DirectedGraph(7)

graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,2)
graph.add_edge(2,4)
graph.add_edge(2,4)
graph.add_edge(3,1)
graph.add_edge(3,2)
graph.add_edge(3,5)
graph.add_edge(4,3)
graph.add_edge(4,6)
graph.add_edge(5,6)
graph.add_edge(6,3)

assert(find_eulerian_path(graph) == [1,3,5,6,3,2,4,3,1,2,2,4,6])

print("PASS")