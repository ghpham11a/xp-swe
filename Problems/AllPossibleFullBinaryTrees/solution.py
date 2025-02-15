# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def all_possible_fbt(self, n):
        cache = {0: [], 1: [TreeNode()]}
        return self.recurse(cache, n)

    def recurse(self, cache, nodes_left):

        if nodes_left in cache:
            return cache[nodes_left]

        output = []
        for left_nodes in range(nodes_left): 
            right_nodes = nodes_left - 1 - left_nodes
            
            left_trees = self.recurse(cache, left_nodes)
            right_trees = self.recurse(cache, right_nodes)

            for t1 in left_trees:
                for t2 in right_trees:
                    output.append(TreeNode(0, t1, t2))

        cache[nodes_left] = output

        return cache[nodes_left]