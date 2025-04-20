# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def good_nodes(self, root):
        return self.dfs(root, root.val)

    def dfs(self, node, max_val):
        if not node:
            return 0

        output = 1 if node.val >= max_val else 0

        max_val = max(max_val, node.val)
        output += self.dfs(node.left, max_val)
        output += self.dfs(node.right, max_val)
        return output