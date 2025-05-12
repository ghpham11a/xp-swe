from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # Helper function to check if the given cell is within matrix bounds
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        # Make a deep copy of the input matrix to store results
        matrix = [row[:] for row in mat]
        m = len(matrix)
        n = len(matrix[0])
        
        # Queue for BFS traversal; stores tuples of (row, col, distance)
        queue = deque()
        
        # Set to keep track of visited cells to prevent revisiting
        seen = set()
        
        # Initialize the queue with all 0-cells as starting points
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    queue.append((row, col, 0))  # distance to self is 0
                    seen.add((row, col))         # mark as visited

        # Possible directions to move in the matrix: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Perform BFS from all 0-cells simultaneously
        while queue:
            row, col, steps = queue.popleft()

            # Explore all neighboring cells
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx

                # Only process unvisited and valid cells
                if (next_row, next_col) not in seen and valid(next_row, next_col):
                    seen.add((next_row, next_col))  # Mark as visited
                    queue.append((next_row, next_col, steps + 1))  # Enqueue with updated distance
                    matrix[next_row][next_col] = steps + 1         # Update distance in result matrix

        # Return the matrix with updated distances
        return matrix