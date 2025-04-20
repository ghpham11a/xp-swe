from collections import deque

class Solution:
    def orangesRotting(self, grid):

        init_fresh_count = 0
        queue = deque()
        time = 0

        for row_index in range(len(grid)):
            for col_index in range(len(grid[0])):
                if grid[row_index][col_index] == 1:
                    init_fresh_count += 1
                if grid[row_index][col_index] == 2:
                    queue.append([row_index, col_index])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue and init_fresh_count > 0:

            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = dr+ r, dc + c
                    # if in bounds and fresh, make rotten
                    if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    queue.append([row, col])
                    init_fresh_count -= 1
            time += 1

        return time if init_fresh_count == 0 else -1