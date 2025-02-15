class DisjointSet:

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] == node:
            self.parent[node] = self.parent[self.parent[node]]
            return self.parent[node]
        return self.find(parent[node])

    def union(self, node_a, node_b):
        root_a = self.find(node_a)
        root_b = self.find(node_b)

        if root_a == root_b:
            return False

        if self.rank[root_a] > self.rank[root_b]:
            self.rank[root_b] = root_a
            self.rank[root_a] += self.rank[root_b]
        else:
            self.rank[root_a] = root_b
            self.rank[root_b] += self.rank[root_a]

        return True

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        val_to_index = defaultdict(list)
        for src, val in enumerate(vals):
            val_to_index[val].append(src)

        output = 0
        disjoint_set = DisjointSet(len(vals))

        for val in sorted(val_to_index.keys()):
            for src in val_to_index[val]:
                for neighbor in graph[src]:
                    if vals[neighbor] <= vals[src]:
                        disjoint_set.union(neighbor, src)
            
            # For each disjoint set, how many val's does it contain
            count = defaultdict(int)
            for src in val_to_index[val]:
                count[disjoint_set.find(src)] += 1
                output += count[disjoint_set.find(src)]

        return output