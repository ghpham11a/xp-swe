# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def bst_from_preorder(self, preorder):
        # Start the recursive construction with:
        # - preorder traversal
        # - index [0] as a mutable reference to track current element
        # - full valid value range (-inf, +inf) for root
        return self.recurse(preorder, [0], float("-inf"), float("inf"))

    def recurse(self, preorder, index, lower, upper):
        # Base case: if all elements have been used, return None
        if index[0] == len(preorder):
            return None

        val = preorder[index[0]]

        # If current value is outside the valid range for this subtree, skip it
        if val < lower or val > upper:
            return None

        # Consume the current value and move to the next index
        index[0] += 1

        # Create the current root node
        root = TreeNode(val)

        # Recursively build the left subtree:
        # - all values must be less than current node value
        root.left = self.recurse(preorder, index, lower, val)

        # Recursively build the right subtree:
        # - all values must be greater than current node value
        root.right = self.recurse(preorder, index, val, upper)

        return root