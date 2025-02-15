from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def find_duplicate_subtrees(self, root):

        sub_trees = defaultdict(list)

        def dfs(node):
            if not node:
                return "null"

            serialization = ",".join([str(node.val), dfs(node.left), dfs(node.right)])

            if len(sub_trees[serialization]) == 1:
                output.append(node)

            sub_trees[serialization].append(node)
            return serialization

        output = []
        dfs(root)

        return output
        