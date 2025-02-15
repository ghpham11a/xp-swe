class Solution:

    def uniqu_paths_with_obstacles(self, obstacle_grid):
        row_count = len(obstacle_grid)
        col_count = len(obstacle_grid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacle_grid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacle_grid[0][0] = 1

        # Filling the values for the first column
        for row_index in range(1, row_count):
            if obstacle_grid[row_index][0] == 0 and obstacle_grid[row_index-1][0] == 1:
                obstacle_grid[row_index][0] = 1
            else:
                obstacle_grid[row_index][0] = 0

        # Filling the values for the first row        
        for col_index in range(1, col_count):
            if obstacle_grid[0][col_index] == 0 and obstacle_grid[0][col_index-1] == 1:
                obstacle_grid[0][col_index] = 1
            else:
                obstacle_grid[0][col_index] = 0

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[row_index][col_index] = cell[row_index - 1][col_index] + cell[row_index][col_index - 1]
        # i.e. From above and left.
        for row_index in range(1, row_count):
            for col_index in range(1, col_count):
                if obstacle_grid[row_index][col_index] == 0:
                    obstacle_grid[row_index][col_index] = obstacle_grid[row_index-1][col_index] + obstacle_grid[row_index][col_index-1]
                else:
                    obstacle_grid[row_index][col_index] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.            
        return obstacle_grid[-1][-1]