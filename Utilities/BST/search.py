# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def search_bst(self, root, val):

        if not root:
            return None

        if val == root.val:
            return root
        
        if val < root.val:
            return self.search_bst(root.left, val)

        if val > root.val:
            return self.search_bst(root.right, val)