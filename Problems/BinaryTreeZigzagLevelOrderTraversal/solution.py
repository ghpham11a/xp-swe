from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def zigzag_level_order(self, root):
        # This will store the final zigzag level order traversal
        output = []

        # Initialize the queue with the root node if it exists
        queue = deque([root] if root else [])

        # Perform BFS traversal
        while queue:
            level = []  # List to store values of the current level

            # Traverse all nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft()  # Pop from front of the queue

                # Determine direction based on current level depth:
                # even index => left to right
                # odd index => right to left
                if len(output) % 2 == 0:
                    level.append(node.val)  # Append to the end
                else:
                    level.insert(0, node.val)  # Insert at the beginning for reverse order

                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append the current level to the output after processing
            output.append(level)

        return output