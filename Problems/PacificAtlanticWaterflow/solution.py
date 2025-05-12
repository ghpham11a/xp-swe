from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])  # Get matrix dimensions
        pac, atl = set(), set()  # Sets to store reachable cells for Pacific and Atlantic oceans

        # Depth-first search to explore cells that can flow to an ocean
        def dfs(r, c, visit, prev_height):
            out_of_bounds = r < 0 or c < 0 or r >= ROWS or c >= COLS
            already_visited = (r, c) in visit
            lower_than_prev = heights[r][c] < prev_height

            # Stop DFS if:
            # 1. Out of bounds
            # 2. Already visited
            # 3. Current cell is lower than previous (water can't flow uphill)
            if out_of_bounds or already_visited or lower_than_prev:
                return
            
            visit.add((r, c))  # Mark current cell as reachable

            # Recursively explore neighboring cells (up, down, left, right)
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Start DFS from all cells along the Pacific border (top row and left column)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])  # Top edge (Pacific)
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])  # Bottom edge (Atlantic)

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])  # Left edge (Pacific)
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])  # Right edge (Atlantic)

        output = []
        # Cells that are reachable by both oceans are included in the result
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    output.append([r, c])
        return output