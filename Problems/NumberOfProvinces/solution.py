class Solution:

    def findCircleNum(self, isConnected):

        output = 0
        visited = set()

        for i in range(len(isConnected)):
            if i not in visited:
                output += 1
                self.dfs(i, visited, isConnected)
        return output

    def dfs(self, city, visited, isConnected):
        visited.add(city)
        for neighbor in range(len(isConnected)):
            if isConnected[city][neighbor] and neighbor not in visited:
                self.dfs(neighbor, visited, isConnected)
        return