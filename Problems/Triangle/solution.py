from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Initialize a DP array with one extra space than the number of rows
        # This array will be used bottom-up to store minimum path sums
        dp = [0] * (len(triangle) + 1)

        # Iterate from the bottom row up to the top row
        for row in triangle[::-1]:
            # For each element in the current row, compute the minimum path sum
            # by adding the current value to the minimum of the two adjacent values from the row below
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i],  dp[i + 1])

        # The final result (minimum path sum from top to bottom) will be stored at dp[0]
        return dp[0]