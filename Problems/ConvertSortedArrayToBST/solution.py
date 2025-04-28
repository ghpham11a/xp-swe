from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # Helper function to recursively build the BST
        def helper(left, right):
            # Base case: if the range is invalid, return None (no node to create)
            if left > right:
                return None

            # Choose the middle element as the root to ensure balance
            m = (left + right) // 2

            # Create a new TreeNode with the middle element
            root = TreeNode(nums[m])

            # Recursively build the left subtree with elements left of middle
            root.left = helper(left, m - 1)

            # Recursively build the right subtree with elements right of middle
            root.right = helper(m + 1, right)

            # Return the constructed subtree rooted at 'root'
            return root

        # Start the recursion with the full array range
        return helper(0, len(nums) - 1)