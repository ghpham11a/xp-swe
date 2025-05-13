from collections import deque
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        # Initialize the queue for BFS, starting with the root node
        queue = deque([root])
        output = []  # This will store the visible nodes from the right side

        while queue:
            right_side = None     # Will hold the rightmost node at the current level
            q_len = len(queue)    # Number of nodes in the current level

            for i in range(q_len):
                node = queue.popleft()  # Process each node in the level

                if node:
                    right_side = node  # Update the rightmost node seen at this level
                    # Add children to queue for the next level
                    queue.append(node.left)
                    queue.append(node.right)

            # After processing the level, add the last non-null node seen to output
            if right_side:
                output.append(right_side.val)

        return output  # Return list of rightmost node values per level