from collections import defaultdict

class Solution:

    def find_eulerian_path(self, graph, start):
        output = []

        self.find_eulerian_path_dfs(graph, output, start)

        return output[::-1]

    def find_eulerian_path_dfs(self, graph, output, node):
        neighbors = graph[node]

        while neighbors:
            dst = neighbors.pop()
            self.find_eulerian_path_dfs(graph, output, dst)

        output.append(node)

    def find_itinerary(self, tickets):
        
        graph = defaultdict(list)

        tickets.sort(reverse=True)

        for src, dst in tickets:
            graph[src].append(dst)

        output = self.find_eulerian_path(graph, "JFK")

        return output

runner = Solution()

assert(runner.find_itinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"])

print("PASS")