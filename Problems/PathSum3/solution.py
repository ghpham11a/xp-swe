from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        self.paths = 0
        self.path_sums = defaultdict(int)
        self.path_sums[0] = 1

        self.dfs(root, 0, targetSum)
        return self.paths

    def dfs(self, node, curr_sum, target_sum):
        if not node:
            return 

        curr_sum += node.val

        self.paths += self.path_sums[curr_sum - target_sum]
        self.path_sums[curr_sum] += 1

        if node.right:
            self.dfs(node.right, curr_sum, target_sum)
        if node.left:
            self.dfs(node.left, curr_sum, target_sum)
        self.path_sums[curr_sum] -= 1