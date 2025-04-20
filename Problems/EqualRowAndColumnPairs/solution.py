from collections import defaultdict

class Solution:
    
    def equal_pairs(self, grid):
        output = 0

        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1

        for col in range(len(grid)):
            column = tuple(grid[r][col] for r in range(len(grid)))
            if column in rows:
                output += rows[column]

        return output