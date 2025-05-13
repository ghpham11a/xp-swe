from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either list is empty, there's no tree to build
        if not preorder or not inorder:
            return None

        # The first element in preorder is always the root of the current subtree
        root = TreeNode(preorder[0])

        # Find the index of the root in the inorder list
        # This tells us how many nodes are in the left subtree
        mid = inorder.index(preorder[0])

        # Recursively build the left subtree:
        # - preorder[1:mid+1] → the next `mid` elements after root belong to the left subtree
        # - inorder[:mid] → elements to the left of `mid` in inorder are part of the left subtree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        # Recursively build the right subtree:
        # - preorder[mid+1:] → remaining elements after the left subtree
        # - inorder[mid+1:] → elements to the right of `mid` are part of the right subtree
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # Return the built tree rooted at `root`
        return root