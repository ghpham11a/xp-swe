from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pseudo_palindromic_paths(self, root):
        count = defaultdict(int)
        odds = [0]

        return self.recurse(count, odds, root)

    def recurse(self, count, odds, node):
        
        if not node:
            return 0

        count[node.val] += 1
        odd_change = 1 if count[node.val] % 2 == 1 else -1
        odds[0] += odd_change

        if not node.left and not node.right:
            res = 1 if odds[0] <= 1 else 0
        else:
            res = self.recurse(count, odds, node.left) + self.recurse(count, odds, node.right)

        odds[0] -= odd_change
        count[node.val] -= 1

        return res