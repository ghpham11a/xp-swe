from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root):

        output = 0
        queue = deque([(root, 1, 0)])
        prev_level = 0
        prev_num = 1

        while queue:

            node, num, level = queue.popleft()

            if level > prev_level:
                prev_level = level
                prev_num = num

            output = max(output, num - prev_num + 1)

            if node.left:
                queue.append((node.left, 2 * num, level + 1))
            if node.right:
                queue.append((node.right, 2 * num + 1, level + 1))

        return output