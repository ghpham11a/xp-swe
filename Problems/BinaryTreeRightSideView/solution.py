from collections import deque
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        queue = deque([root])
        output = []

        while queue:

            right_side = None
            q_len = len(queue)

            for i in range(q_len):
                node = queue.popleft()
                if node:
                    right_side = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if right_side:
                output.append(right_side.val)
        return output