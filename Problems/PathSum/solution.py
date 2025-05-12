from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the tree is empty, no path exists
        if not root:
            return False

        # Subtract the current node's value from targetSum
        targetSum -= root.val

        # If we've reached a leaf node, check if the remaining sum is 0
        if not root.left and not root.right:
            return targetSum == 0

        # Recursively check the left and right subtrees
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)