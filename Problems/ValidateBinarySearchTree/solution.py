import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def is_valid_bst(self, root):
        # Start DFS traversal with initial min/max bounds
        return self.dfs(root)
        
    def dfs(self, node, low = -math.inf, high = math.inf):
        # An empty node/subtree is valid
        if not node:
            return True

        # Current node's value must be strictly within (low, high) range
        if node.val <= low or node.val >= high:
            return False

        # Recursively validate the left subtree
        # All values in the left subtree must be < current node's value
        left_result = self.dfs(node.left, low, node.val)

        # Recursively validate the right subtree
        # All values in the right subtree must be > current node's value
        right_result = self.dfs(node.right, node.val, high)

        # Tree is valid only if both left and right subtrees are valid
        return left_result and right_result