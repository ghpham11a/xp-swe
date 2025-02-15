# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def largest_values(self, root):
        output = []

        if not root:
            return output
            
        self.level_order_recurse(root, output, 0)

        return output

    def level_order_recurse(self, node, output, level):
        # start the current level
        if len(output) == level:
            output.append(float("-inf"))

        # append the current node value
        if node.val > output[level]:
            output[level] = node.val

        # process child nodes for the next level
        if node.left:
            self.level_order_recurse(node.left, output, level + 1)
        if node.right:
            self.level_order_recurse(node.right, output, level + 1)