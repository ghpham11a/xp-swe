class Solution:

    def can_finish(self, numCourses, prerequisites):
        
        graph = defaultdict(list)
        markers = {}

        for dst, src in prerequisites:
            graph[src].append(dst)

        try:
            for node in range(numCourses):
                if node not in markers:
                    self.dfs(graph, markers, node)
        except:
            return False

        return True

    def dfs(self, graph, markers, node):

        if node in markers and markers[node] == True:
            return

        if node in markers and markers[node] == False:
            raise Exception("Cycle detected")

        markers[node] = False

        for neighbor in graph[node]:
            self.dfs(graph, markers, neighbor)

        markers[node] = True

solution = Solution()

assert(solution.can_finish(2, [[1,0]]) == True)

print("PASS")