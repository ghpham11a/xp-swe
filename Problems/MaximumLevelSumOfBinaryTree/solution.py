

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root):
        queue = [root]

        max_sum = root.val
        max_level = 1
        level_num = 1

        while queue:

            next_level = []
            level_sum = 0
            level_num += 1

            for node in queue:
                if node.left:
                    next_level.append(node.left)
                    level_sum += node.left.val
                if node.right:
                    next_level.append(node.right)
                    level_sum += node.right.val
            if next_level != [] and level_sum > max_sum:
                max_sum = level_sum
                max_level = level_num
            queue = next_level

        return max_level