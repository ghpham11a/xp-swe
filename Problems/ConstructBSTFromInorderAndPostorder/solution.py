from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # Base case: if inorder list is empty, no nodes to construct
        if not inorder:
            return None

        # The last element in postorder is always the root of the current subtree
        root = TreeNode(postorder.pop())

        # Find the index of the root in the inorder list to split left and right subtrees
        idx = inorder.index(root.val)

        # Build the right subtree first because postorder is left-right-root,
        # and we're consuming postorder from the end
        root.right = self.buildTree(inorder[idx + 1:], postorder)

        # Build the left subtree
        root.left = self.buildTree(inorder[:idx], postorder)

        # Return the constructed tree root
        return root
