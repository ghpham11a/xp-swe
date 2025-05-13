from collections import defaultdict

# Union-Find (Disjoint Set Union) class to group accounts based on shared emails
class DisjointSet(object):
    def __init__(self, size):
        # Each node starts as its own parent (self-rooted)
        self.parent = [n for n in range(size)]
        # Rank array helps to optimize union by attaching smaller trees under larger ones
        self.rank = [1] * size 

    def find(self, node):
        # Path compression optimization: point node directly to root
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_a, node_b):
        # Find root parents of both nodes
        root_a = self.find(node_a)
        root_b = self.find(node_b)

        # If they already share the same root, they are already in the same group
        if root_a == root_b:
            return False

        # Union by rank: attach smaller tree under the bigger one
        if self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1
        else:
            self.parent[root_a] = root_b
            self.rank[root_b] += 1

        return True

class Solution(object):
    def accounts_merge(self, accounts):
        # Initialize disjoint set structure for all accounts
        disjoint_set = DisjointSet(len(accounts))
        email_to_acct = {}  # Maps email to account index

        # Step 1: Union accounts if they share any email
        for index, account in enumerate(accounts):
            for email in account[1:]:  # Skip the name at index 0
                if email in email_to_acct:
                    # If email seen before, union current account with previous one
                    disjoint_set.union(index, email_to_acct[email])
                else:
                    # Otherwise, map email to current account
                    email_to_acct[email] = index

        # Step 2: Group emails by their final root parent (leader) in the union-find structure
        email_to_group = defaultdict(list)
        for email, index in email_to_acct.items():
            leader = disjoint_set.find(index)  # Get the representative of the account group
            email_to_group[leader].append(email)

        # Step 3: Build the final output
        output = []
        for index, emails in email_to_group.items():
            name = accounts[index][0]  # Use the name associated with the group leader
            output.append([name] + sorted(emails))  # Append name + sorted email list

        return output

solution = Solution()

test_input_1 = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
test_output_1 = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
assert(solution.accounts_merge(test_input_1) == test_output_1)

print("PASS")