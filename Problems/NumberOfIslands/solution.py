from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        output = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    output += 1
                    self.dfs(row, col, grid)
        return output

    def dfs(self, row, col, grid):

        if not self.is_valid(row, col, grid):
            return

        grid[row][col] = "."

        self.dfs(row + 1, col, grid)
        self.dfs(row - 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row, col - 1, grid)

        pass

    def is_valid(self, row, col, grid):

        if row < 0 or row >= len(grid):
            return False

        if col < 0 or col >= len(grid[0]):
            return False

        if grid[row][col] != "1":
            return False

        return True