# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def bst_from_preorder(self, preorder):
        return self.recurse(preorder, [0], float("-inf"), float("inf"))

    def recurse(self, preorder, index, lower, upper):

        # If all elements from peorder are used, then tree is constructed
        if index[0] == len(preorder):
            return None

        val = preorder[index[0]]

        # If current element couldn't be placed here to meet BST requirements
        if val < lower or val > upper:
            return None

        # place current element and recursively construct subtrees
        index[0] += 1
        root = TreeNode(val)
        root.left = self.recurse(preorder, index, lower, val)
        root.right = self.recurse(preorder, index, val, upper)

        return root