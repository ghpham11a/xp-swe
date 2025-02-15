# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def flip_equiv(self, root1, root2):

        if not root1 or not root2:
            return root1 == root2

        if root1.val != root2.val:
            return False

        is_equal_before_flip = self.flip_equiv(root1.left, root2.left) and self.flip_equiv(root1.right, root2.right)

        is_equal_after_flip = self.flip_equiv(root1.left, root2.right) and self.flip_equiv(root1.right, root2.left)

        return is_equal_before_flip or is_equal_after_flip