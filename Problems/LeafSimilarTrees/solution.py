# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        node1_output = []
        self.dfs(root1, node1_output)

        node2_output = []
        self.dfs(root2, node2_output)

        return node1_output == node2_output

    def dfs(self, node, output):
        if not node:
            return output

        if not node.left and not node.right:
            output.append(node.val)

        self.dfs(node.left, output)
        self.dfs(node.right, output)
        