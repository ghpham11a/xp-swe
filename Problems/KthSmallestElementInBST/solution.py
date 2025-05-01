from typing import Optional
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []  # Stack to simulate recursive in-order traversal

        while True:
            # Go as left as possible from the current node
            while root:
                stack.append(root)  # Push current node to stack
                root = root.left     # Move to left child

            # Pop the node from the top of the stack
            root = stack.pop()
            k -= 1  # We've now visited one more node in in-order sequence

            # If k is 0, we've reached the kth smallest element
            if not k:
                return root.val

            # Move to the right child to continue in-order traversal
            root = root.right

solution = Solution()

assert(solution.combination_sum_3([3,2,1,5,6,4], 2) == 5)

print("PASS")