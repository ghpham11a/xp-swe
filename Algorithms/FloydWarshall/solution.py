
POSITIVE_INFINITY = float("inf")
NEGATIVE_INFINITY = -float("inf")

def floyd_warshall(matrix):
    # Determine the number of vertices in the graph (assumed to be a square matrix)
    matrix_len = len(matrix)

    # Create a deep copy of the input matrix to store distances.
    # This avoids modifying the original matrix.
    dist = [row[:] for row in matrix]

    # Main loop of Floyd-Warshall:
    # k is the intermediate vertex we consider for potential shorter paths.
    for k in range(matrix_len):
        # Loop over every possible source vertex.
        for src in range(matrix_len):
            # Loop over every possible destination vertex.
            for dst in range(matrix_len):
                # If the path from src to k and then from k to dst is shorter
                # than the currently recorded distance from src to dst, update it.
                if dist[src][k] + dist[k][dst] < dist[src][dst]:
                    dist[src][dst] = dist[src][k] + dist[k][dst]

    # Check for negative cycles in the graph.
    # A negative cycle exists if a vertex can reach itself with a negative cost.
    # For each vertex k, if there is a negative cycle (i.e., dist[k][k] < 0),
    # then for any pair of vertices (src, dst) that can reach k,
    # the shortest distance is effectively negative infinity.
    for k in range(matrix_len):
        for src in range(matrix_len):
            for dst in range(matrix_len):
                # Only update if both subpaths (src->k and k->dst) are reachable
                # and a negative cycle is detected at vertex k.
                if (dist[src][k] != POSITIVE_INFINITY and 
                    dist[k][dst] != POSITIVE_INFINITY and 
                    dist[k][k] < 0):
                    dist[src][dst] = NEGATIVE_INFINITY

    # Return the matrix containing shortest distances (or negative infinity where applicable)
    return dist


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

all_pairs_shortest_path = floyd_warshall(adjacency_matrix)

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

print("PASS")