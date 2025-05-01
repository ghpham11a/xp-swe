
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        # Recursive function to build the quad-tree
        def dfs(n, r, c):
            # Check if all cells in the n x n subgrid starting at (r, c) are the same
            all_same = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        all_same = False  # Found a different value in the subgrid
                        break

            if all_same:
                # If all values are the same, return a leaf node with that value
                return Node(grid[r][c], True)

            # Otherwise, split the grid into 4 quadrants and recursively build subtrees
            n = n // 2  # Reduce size for the 4 subgrids (since n is always a power of 2)

            top_left = dfs(n, r, c)
            top_right = dfs(n, r, c + n)
            bottom_left = dfs(n, r + n, c)
            bottom_right = dfs(n, r + n, c + n)

            # Return a parent node that is not a leaf and contains the 4 sub-quads
            return Node(0, False, top_left, top_right, bottom_left, bottom_right)

        # Start DFS from the top-left corner of the full grid
        return dfs(len(grid), 0, 0)