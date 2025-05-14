from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Helper function to compute the depth of the tree.
    # It goes all the way down the leftmost path.
    def compute_depth(self, node: TreeNode) -> int:
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    # Helper function to determine if a node exists at index `idx`
    # in the last level, given depth `d`, by traversing the tree using binary pathing.
    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        left, right = 0, 2**d - 1  # Range of indices at the last level
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left  # Move left in the tree
                right = pivot     # Update right bound
            else:
                node = node.right  # Move right in the tree
                left = pivot + 1   # Update left bound
        return node is not None  # If node is found, it exists

    def countNodes(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, return 0
        if not root:
            return 0

        # Compute the depth of the tree (number of edges to the last level)
        d = self.compute_depth(root)

        # If the tree only has the root node
        if d == 0:
            return 1

        # Binary search range for the number of nodes in the last level
        # Last level can have up to 2^d nodes, indexed from 0 to 2^d - 1
        left, right = 1, 2**d - 1

        # Perform binary search to count how many nodes exist on the last level
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                # Node exists at this index, search further right
                left = pivot + 1
            else:
                # Node does not exist, search left
                right = pivot - 1

        # Total nodes = nodes above last level + nodes in last level
        # Nodes above last level = 2^d - 1 (perfectly filled)
        # Nodes in last level = left (binary search converges here)
        return (2**d - 1) + left