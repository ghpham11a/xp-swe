import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def is_valid_bst(self, root):
        return self.dfs(root)
        
    def dfs(self, node, low = -math.inf, high = math.inf):

        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False

        left_result = self.dfs(node.left, low, node.val)
        right_result = self.dfs(node.right, node.val, high)

        return (left_result and right_result)