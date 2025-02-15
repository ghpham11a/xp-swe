class DisjointSet:

    def __init__(self, size):
        self.parent =  [n for n in range(size)]
        self.rank = [1] * size

    def find(self, node):
        if self.parent[node] == node:
            self.parent[node] = self.parent[self.parent[node]]
            return self.parent[node]
        return self.find(self.parent[node])

    def union(self, node_a, node_b):
        root_a = self.find(node_a)
        root_b = self.find(node_b)

        if root_a == root_b:
            return False

        if self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
            self.rank[root_a] += self.rank[root_b]
        else:
            self.parent[root_a] = root_b
            self.rank[root_b] += self.rank[root_a]

        return True

class Solution:

    def find_redundant_connection(self, edges):

        disjoint_set = DisjointSet(len(edges) + 1)

        for edge in edges:
            if disjoint_set.union(*edge) == False:
                return edge

        return []

solution = Solution()

assert(solution.find_redundant_connection([[1,2],[1,3],[2,3]]) == [2,3])

print("PASS")