from collections import defaultdict

class Solution:

    VISITED = -1
    VISITED_NO_CYCLE = 1

    def find_order(self, num_courses, prerequisites):

        graph = defaultdict(list)
        visited = [False] * num_courses
        output = []

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        for course in range(num_courses):
            if not self.dfs(course, graph, output, visited):
                return []

        return output[::-1] 


    def dfs(self, node, graph, output, visited):

        if visited[node] == self.VISITED:
            return False
        if visited[node] == self.VISITED_NO_CYCLE:
            return True
        
        visited[node] = self.VISITED
        
        for neighbor in graph[node]:
            if not self.dfs(neighbor, graph, output, visited):
                return False

        visited[node] = self.VISITED_NO_CYCLE

        output.append(node)

        return True

solution = Solution()

assert(solution.find_order(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,2,1,3])
assert(solution.find_order(2, [[0,1],[1,0]]) == [])

print("PASS")