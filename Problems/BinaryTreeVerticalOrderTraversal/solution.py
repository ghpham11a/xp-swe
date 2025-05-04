from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            # If the tree is empty, return an empty list
            return []

        from collections import defaultdict, deque

        # A hashmap to collect nodes grouped by their column index
        columnTable = defaultdict(list)

        # Track the min and max column indices encountered
        min_column = max_column = 0

        # Queue for level-order traversal (BFS), storing (node, column index)
        queue = deque([(root, 0)])

        while queue:
            # Dequeue a node and its associated column index
            node, column = queue.popleft()

            if node is not None:
                # Append the node's value to the corresponding column in the table
                columnTable[column].append(node.val)

                # Update the boundaries of the column range
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # Enqueue left and right children with updated column indices
                queue.append((node.left, column - 1))   # Left child goes one column to the left
                queue.append((node.right, column + 1))  # Right child goes one column to the right

        # Extract and return the result list ordered from leftmost column to rightmost
        return [columnTable[x] for x in range(min_column, max_column + 1)]