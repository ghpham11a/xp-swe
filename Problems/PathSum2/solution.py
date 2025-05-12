from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []  # This will store all valid root-to-leaf paths with the required sum
        
        # Start depth-first search from the root
        self.dfs(root, targetSum, [], output)

        return output

    def dfs(self, node, target_sum, path, output):
        # Base case: if the current node is None, return (end of a path)
        if not node:
            return

        # Subtract the current node's value from the remaining sum
        curr_sum = target_sum - node.val

        # Add the current node's value to the current path
        path.append(node.val)

        # Check if this is a leaf node and the remaining sum is zero
        if curr_sum == 0 and not node.left and not node.right:
            # A valid path is found; append a copy of the path to the output
            output.append(path.copy())
        else:
            # Continue DFS on the left and right children
            self.dfs(node.left, curr_sum, path, output)
            self.dfs(node.right, curr_sum, path, output)

        # Backtrack: remove the current node's value before returning to the previous level
        path.pop()