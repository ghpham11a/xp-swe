from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_complete_tree(self, root):
        # Initialize a queue for level-order traversal (BFS)
        queue = deque([root])

        # Process nodes level by level
        while queue:
            current = queue.popleft()

            if current:
                # If the current node is not null, enqueue its children (could be null)
                queue.append(current.left)
                queue.append(current.right)
            else:
                # If a null is encountered, then all following nodes must be null
                # If we find any non-null node after this, it's not a complete binary tree
                while queue:
                    if queue.popleft():
                        return False  # Found a non-null node after a null, invalid

        # If we finish the traversal without breaking the rules, it's complete
        return True