from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_complete_tree(self, root):
        queue = deque([root])

        while queue:
            current = queue.popleft()

            if current:
                queue.append(current.left)
                queue.append(current.right)
            else:
                while queue:
                    if queue.popleft():
                        return False

        return True