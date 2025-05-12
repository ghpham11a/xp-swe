class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, there is no path
        if not root:
            return 0

        output = [0]  # Stores the maximum univalue path length found

        # Start DFS traversal from the root
        self.dfs(root, root.val, output)

        return output[0]  # Return the maximum path length found

    def dfs(self, node, parent, output):
        # Base case: if current node is None, return 0
        if not node:
            return 0

        # Recursively find longest univalue path in the left subtree
        left = self.dfs(node.left, node.val, output)

        # Recursively find longest univalue path in the right subtree
        right = self.dfs(node.right, node.val, output)

        # Update the global maximum path if the current node connects valid left + right paths
        output[0] = max(output[0], left + right)

        # If current node value matches its parent's value, it can be part of the path
        if node.val == parent:
            # Return the longest one-side path that can be extended upward
            return max(left, right) + 1
        else:
            # Otherwise, it can't contribute to the parent path
            return 0