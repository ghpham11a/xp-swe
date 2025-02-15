from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzag_level_order(self, root):

        output = []
        queue = deque([root] if root else [])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()

                if len(output) % 2 == 0:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            output.append(level)

        return output