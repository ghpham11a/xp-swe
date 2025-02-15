# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowest_common_ancestor(self, root, p, q):
        # Traverse the tree
        output = [None]
        self.recurse_tree(p, q, output, root)
        return output[0]

    def recurse_tree(self, p, q, output, current_node):

        # If reached the end of a branch, return False.
        if not current_node:
            return False

        # Left Recursion
        left = self.recurse_tree(p, q, output, current_node.left)

        # Right Recursion
        right = self.recurse_tree(p, q, output, current_node.right)

        # If the current node is one of p or q
        mid = current_node == p or current_node == q

        # If any two of the three flags left, right or mid become True.
        if mid + left + right >= 2:
            output[0] = current_node

        # Return True if either of the three bool values is True.
        return mid or left or right