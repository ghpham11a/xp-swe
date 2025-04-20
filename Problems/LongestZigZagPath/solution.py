# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def longest_zig_zag(self, root):
        self.path = 0

        self.dfs(root.right, False, 1)
        self.dfs(root.left, True, 1)

        return self.path

    def dfs(self, node, from_left, curr):
        if node is None:
            return

        self.path = max(self.path, curr)

        if from_left:
            self.dfs(node.right, False, curr + 1)
            self.dfs(node.left, True, 1)
        else:
            self.dfs(node.right, False, 1)
            self.dfs(node.left, True, curr + 1)