# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if the current node is null, the depth is 0
        if root is None:
            return 0

        # Recursively compute the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # The depth of the tree rooted at this node is 1 (for the current node)
        # plus the maximum depth of its left or right subtree
        return 1 + max(left_depth, right_depth)