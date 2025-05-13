from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []  # List to store values at each level

        queue = deque()
        queue.append(root)  # Initialize queue with the root node for BFS

        while queue:
            level = []  # Temporary list to store values for current level

            # Process all nodes at the current level
            for i in range(len(queue)):
                node = queue.popleft()  # Dequeue current node

                if node:
                    level.append(node.val)  # Add node's value to current level list

                    # Add child nodes to queue for next level processing
                    queue.append(node.left)
                    queue.append(node.right)

            # Only add level list to results if it's not empty
            if level:
                levels.append(level)

        output = []
        # Calculate average of each level and store in output
        for level in levels:
            output.append(sum(level) / len(level))

        return output