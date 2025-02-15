from collections import defaultdict

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
            self.rank[root_a] += 1
        else:
            self.parent[root_a] = root_b
            self.rank[root_b] += 1

        return True

class Solution(object):

    def accounts_merge(self, accounts):
        
        disjoint_set = DisjointSet(len(accounts))
        email_to_acct = {}

        for index, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acct:
                    disjoint_set.union(index, email_to_acct[email])
                else:
                    email_to_acct[email] = index

        email_to_group = defaultdict(list)
        for email, index in email_to_acct.items():
            leader = disjoint_set.find(index)
            email_to_group[leader].append(email)

        output = []
        for index, emails in email_to_group.items():
            name = accounts[index][0]
            output.append([name] + sorted(email_to_group[index]))

        return output

solution = Solution()

test_input_1 = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
test_output_1 = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
assert(solution.accounts_merge(test_input_1) == test_output_1)

print("PASS")