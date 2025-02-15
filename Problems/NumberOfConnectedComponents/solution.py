class DisjointSet:

    def __init__(self, size):
        self.parent = [i for i in range(size)]
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
            self.rank[root_a] += 1
        else:
            self.parent[root_a] = root_b
            self.rank[root_b] += 1

        return True

class Solution:
    def count_components(self, n, edges):
        disjoint_set = DisjointSet(n)

        output = n

        for edge in edges:
            if disjoint_set.union(*edge):
                output -= 1

        return output

solution = Solution()

assert(solution.count_components(5, [[0,1],[1,2],[3,4]]) == 2)

print("PASS")