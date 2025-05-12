from collections import defaultdict

class Solution:
    def valid_tree(self, n, edges):
        # Edge case: if there are no nodes, we can consider it a valid (empty) tree
        if not n:
            return True

        # Build the adjacency list for the undirected graph
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = set()  # Keep track of visited nodes during DFS

        # Run DFS starting from node 0. Also track the previous node to avoid counting the parent as a cycle.
        no_graph_cycle = self.dfs(graph, visited, 0, -1)

        # Check that all nodes were visited (i.e., the graph is connected)
        all_nodes_visited = len(visited) == n

        # The graph is a valid tree if it is acyclic and connected
        return no_graph_cycle and all_nodes_visited

    def dfs(self, graph, visited, node, prev_node):
        # If we've already seen this node, we found a cycle
        if node in visited:
            return False

        visited.add(node)  # Mark the node as visited

        for neighbor in graph[node]:
            # Skip the node we came from to prevent false cycle detection
            if neighbor == prev_node:
                continue

            # If DFS on a neighbor detects a cycle, return False
            if not self.dfs(graph, visited, neighbor, node):
                return False

        # No cycle found from this path
        return True

solution = Solution()

assert(solution.valid_tree(5, [[0,1],[0,2],[0,3],[1,4]]) == True)

print("PASS")