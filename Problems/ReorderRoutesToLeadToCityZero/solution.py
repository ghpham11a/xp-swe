class Solution:

    def min_reorder(self, n: int, connections):
        # start at city 0
        # recursively check its neighbors
        # count outgoing edges

        edges = { (a,b) for a, b in connections }
        neighbors = { city:[] for city in range(n) }
        visited = set()
        changes = [0]

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        visited.add(0)
        self.dfs(0, edges, neighbors, visited, changes)

        return changes[0]

    def dfs(self, city, edges, neighbors, visited, changes):

        for neighbor in neighbors[city]:
            if neighbor in visited:
                continue

            # check if this neighbor can reach city 0
            if (neighbor, city) not in edges:
                changes[0] += 1
            visited.add(neighbor)
            self.dfs(neighbor, edges, neighbors, visited, changes)