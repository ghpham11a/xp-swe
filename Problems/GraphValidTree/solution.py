from collections import defaultdict

class Solution:

    def valid_tree(self, n, edges):

        if not n:
            return True

        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = set()

        no_graph_cyle = self.dfs(graph, visited, 0, -1)
        all_nodes_visited = len(visited) == n

        return no_graph_cyle and all_nodes_visited

        
    def dfs(self, graph, visited, node, prev_node):

        if node in visited:
            return False

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor == prev_node:
                continue

            if not self.dfs(graph, visited, neighbor, node):
                return False

        return True

solution = Solution()

assert(solution.valid_tree(5, [[0,1],[0,2],[0,3],[1,4]]) == True)

print("PASS")