from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        # Start the recursive depth-first flattening from the root
        self.dfs(root)

    def dfs(self, root: TreeNode):
        if not root:
            return None  # Base case: if node is None, return None

        # Recursively flatten the left and right subtrees
        left_tail = self.dfs(root.left)   # Tail of the flattened left subtree
        right_tail = self.dfs(root.right) # Tail of the flattened right subtree

        if root.left:
            # Connect the tail of the flattened left subtree to the start of the right subtree
            left_tail.right = root.right

            # Move the entire left subtree to the right side
            root.right = root.left

            # Set the left pointer to None as per problem constraints
            root.left = None

        # Return the tail node of the whole flattened subtree rooted at this node
        # Priority: right_tail > left_tail > root (in case both subtrees are empty)
        last = right_tail or left_tail or root
        return last