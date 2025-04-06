
POSITIVE_INFINITY = float("inf")
NEGATIVE_INFINITY = -float("inf")

def floyd_warshall(matrix):

    matrix_len = len(matrix)

    dist = [row[:] for row in matrix]
    next_node = [[None for _ in range(matrix_len)] for _ in range(matrix_len)]

    for src in range(matrix_len):
        for dst in range(matrix_len):
            if matrix[src][dst] != POSITIVE_INFINITY:
                next_node[src][dst] = dst

    for k in range(matrix_len):
        for src in range(matrix_len):
            for dst in range(matrix_len):
                if dist[src][k] + dist[k][dst] < dist[src][dst]:
                    dist[src][dst] = dist[src][k] + dist[k][dst]
                    next_node[src][dst] = next_node[src][k]

    # check for negative cycle
    for k in range(matrix_len):
        for src in range(matrix_len):
            for dst in range(matrix_len):
                if dist[src][k] != POSITIVE_INFINITY and dist[k][dst] != POSITIVE_INFINITY and dist[k][k] < 0:
                    dist[src][dst] = NEGATIVE_INFINITY
                    next_node[src][dst] = -1

    return dist, next_node

def reconstruct_shortest_path(dist, next_nodes, start, end):
    path = []
    if dist[start][end] == POSITIVE_INFINITY:
        return path
    at = start
    while at != end:
        # Return None since there are an infinite number of shortest paths.
        if at == -1:
            return None
        path.append(at)
        at = next_nodes[at][end]
    # Return None since there are an infinite number of shortest paths.
    if next_nodes[at][end] == -1:
        return None
    path.append(end)
    return path 


adjacency_matrix = [[0 if i == j else float('inf') for j in range(7)] for i in range(7)]

adjacency_matrix[0][1] = 2
adjacency_matrix[0][2] = 5
adjacency_matrix[0][6] = 10
adjacency_matrix[1][2] = 2
adjacency_matrix[1][4] = 11
adjacency_matrix[2][6] = 2
adjacency_matrix[6][5] = 11
adjacency_matrix[4][5] = 1
adjacency_matrix[5][4] = -2

all_pairs_shortest_path, next_nodes = floyd_warshall(adjacency_matrix)

expected_all_pairs_shortest_path = [
    [0, 2, 4, POSITIVE_INFINITY, NEGATIVE_INFINITY, NEGATIVE_INFINITY, 6],
    [POSITIVE_INFINITY, 0, 2, POSITIVE_INFINITY, NEGATIVE_INFINITY, NEGATIVE_INFINITY, 4],
    [POSITIVE_INFINITY, POSITIVE_INFINITY, 0, POSITIVE_INFINITY, NEGATIVE_INFINITY, NEGATIVE_INFINITY, 2],
    [POSITIVE_INFINITY, POSITIVE_INFINITY, POSITIVE_INFINITY, 0, POSITIVE_INFINITY, POSITIVE_INFINITY, POSITIVE_INFINITY],
    [POSITIVE_INFINITY, POSITIVE_INFINITY, POSITIVE_INFINITY, POSITIVE_INFINITY, NEGATIVE_INFINITY, NEGATIVE_INFINITY, POSITIVE_INFINITY],
    [POSITIVE_INFINITY, POSITIVE_INFINITY, POSITIVE_INFINITY, POSITIVE_INFINITY, NEGATIVE_INFINITY, NEGATIVE_INFINITY, POSITIVE_INFINITY],
    [POSITIVE_INFINITY, POSITIVE_INFINITY, POSITIVE_INFINITY, POSITIVE_INFINITY, NEGATIVE_INFINITY, NEGATIVE_INFINITY, 0]
]

assert(all_pairs_shortest_path == expected_all_pairs_shortest_path)

assert(reconstruct_shortest_path(all_pairs_shortest_path, next_nodes, 1, 6) == [1, 2, 6])
assert(reconstruct_shortest_path(all_pairs_shortest_path, next_nodes, 0, 2) == [0, 1, 2])
assert(reconstruct_shortest_path(all_pairs_shortest_path, next_nodes, 1, 4) == None)

print("PASS")