# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def good_nodes(self, root):
        # Start DFS traversal from the root
        # The root is always a "good" node, so we initialize max_val with root's value
        return self.dfs(root, root.val)

    # Helper DFS function that traverses the tree
    # node: the current node being visited
    # max_val: the maximum value encountered so far along the path from the root to this node
    def dfs(self, node, max_val):
        # Base case: if the node is None, return 0 (no good nodes in an empty subtree)
        if not node:
            return 0

        # If the current node's value is greater than or equal to all previous values,
        # it is considered a good node
        output = 1 if node.val >= max_val else 0

        # Update the maximum value for the path to children
        max_val = max(max_val, node.val)

        # Recursively check left and right subtrees, adding their good node counts
        output += self.dfs(node.left, max_val)
        output += self.dfs(node.right, max_val)

        # Return total number of good nodes in this subtree
        return output