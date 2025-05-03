from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0  # Handle empty matrix edge case

        # Initialize a (rows+1) x (cols+1) DP table with all 0s
        # dp[i][j] will represent the size of the largest square 
        # whose bottom-right corner is at cell (i-1, j-1) in the original matrix
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        maxsqlen = 0  # To track the maximum side length of any square of 1s found

        # Start from 1 to leverage the extra padding row/column (makes boundary checks easier)
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                # Only proceed if the current cell in the original matrix is '1'
                if matrix[i - 1][j - 1] == "1":
                    # Compute the minimum of the three neighbors: left, top, and top-left
                    # Add 1 to represent expanding the square
                    dp[i][j] = (
                        min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                    )
                    # Update the global max side length if needed
                    maxsqlen = max(maxsqlen, dp[i][j])

        # Return the area of the largest square found
        return maxsqlen * maxsqlen