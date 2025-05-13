# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        output = []  # This list will store the result of the preorder traversal

        # If the tree is empty, return an empty list
        if root is None:
            return output

        # Stack is used to simulate recursion and track nodes to visit
        stack = [root]

        while stack:
            current = stack.pop()  # Pop the top node from the stack

            if current is not None:
                # Preorder: process the current node before its children
                output.append(current.val)

                # Push right child first so that left child is processed first
                # (stack is LIFO: Last In, First Out)
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)

        return output  # Return the collected node values in preorder