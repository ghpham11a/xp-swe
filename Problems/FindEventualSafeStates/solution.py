class Solution:

    def eventual_safe_nodes(self, graph):
        safe_nodes = {}

        result = []
        for node in range(len(graph)):
            if self.dfs(graph, safe_nodes, node):
                result.append(node)
        return result

    def dfs(self, graph, safe_nodes, node):

        if node in safe_nodes:
            return safe_nodes[node]

        safe_nodes[node] = False

        for neighbor in graph[node]:
            if not self.dfs(graph, safe_nodes, neighbor):
                return False

        safe_nodes[node] = True
        return safe_nodes[node] 

solution = Solution()

assert(solution.eventual_safe_nodes([[1,2],[2,3],[5],[0],[5],[],[]]) == [2, 4, 5, 6])

print("PASS")
