edges = [
    ["i", "j"],
    ["k", "k"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]

def undirected_path(edges, src, dst):
    graph = build_graph(edges)
    return has_path(graph, src, dst, set())

def build_graph(edges):
    graph = {}

    for edge in edges:
        node_a, node_b = edge[0], edge[1]

        if node_a not in graph:
            graph[node_a] = []
        if node_b not in graph:
            graph[node_b] = []

        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    return graph

def has_path(graph, src, dst, visited):
    if src == dst: return True
    if src in visited: return False

    visited.add(src)

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited) == True:
            return True

    return False