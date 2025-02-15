class DisjointSet(object):

    def __init__(self, size):
        self.parent = [n for n in range(size)]
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

edges = [[0,2],[1,4],[1,5],[2,3],[2,7],[4,8],[5,8]]

disjoint_set = DisjointSet(9)

for edge in edges:
    disjoint_set.union(*edge)

assert(disjoint_set.parent == [2, 4, 2, 2, 4, 4, 6, 2, 4])

print("PASS")