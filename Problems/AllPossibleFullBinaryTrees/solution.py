# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def all_possible_fbt(self, n):
        # A cache (memoization) dictionary to store results of subproblems
        # Base cases:
        # - No full binary trees possible with 0 nodes
        # - Exactly one full binary tree with 1 node (a single root node)
        cache = {0: [], 1: [TreeNode()]}
        return self.recurse(cache, n)

    def recurse(self, cache, nodes_left):
        # If already computed for 'nodes_left', return cached result
        if nodes_left in cache:
            return cache[nodes_left]

        output = []

        # Loop over all possible splits of nodes between left and right subtrees
        for left_nodes in range(nodes_left):
            right_nodes = nodes_left - 1 - left_nodes  # Subtract 1 for the current root node

            # Recursively get all full binary trees for left and right subtree sizes
            left_trees = self.recurse(cache, left_nodes)
            right_trees = self.recurse(cache, right_nodes)

            # Combine each left and right subtree to form new trees
            for t1 in left_trees:
                for t2 in right_trees:
                    # Create a new root node with left and right children
                    output.append(TreeNode(0, t1, t2))

        # Memoize the result for current nodes_left
        cache[nodes_left] = output
        return cache[nodes_left]