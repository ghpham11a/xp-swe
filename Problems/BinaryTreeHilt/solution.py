# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTilt(self, root: TreeNode) -> int:

        total_tilt = [0]

        def valueSum(node, total_tilt):

            if not node:
                return 0

            left_sum = valueSum(node.left, total_tilt)
            right_sum = valueSum(node.right, total_tilt)
            tilt = abs(left_sum - right_sum)
            total_tilt[0] += tilt

            return left_sum + right_sum + node.val

        valueSum(root, total_tilt)

        return total_tilt[0]