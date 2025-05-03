import math

from typing import List 

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # Handle special cases: no prices or no transactions allowed
        if not prices or k == 0:
            return 0

        # Optimization: if k is large enough (more than n/2), treat it as unlimited transactions
        if k * 2 >= n:
            res = 0
            # Sum up all profitable upward movements (i.e., local maxima)
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
            return res

        # Initialize a 3D DP array:
        # dp[i][j][h] is the max profit on day i with j transactions used and holding status h
        # h = 0 -> not holding stock, h = 1 -> currently holding stock
        dp = [[[-math.inf] * 2 for _ in range(k + 1)] for _ in range(n)]

        # Base cases:
        dp[0][0][0] = 0                  # Day 0, 0 transactions used, not holding: 0 profit
        dp[0][1][1] = -prices[0]         # Day 0, 1 transaction used (a buy), holding: -price

        # Fill the DP table
        for i in range(1, n):            # Loop over days
            for j in range(k + 1):       # Loop over number of transactions used so far
                # Case 1: Not holding stock
                # Either we were not holding before, or we sell today
                dp[i][j][0] = max(
                    dp[i - 1][j][0],          # Do nothing
                    dp[i - 1][j][1] + prices[i]  # Sell today
                )
                # Case 2: Holding stock
                # Only if we have transaction(s) left to buy
                if j > 0:
                    dp[i][j][1] = max(
                        dp[i - 1][j][1],       # Do nothing
                        dp[i - 1][j - 1][0] - prices[i]  # Buy today
                    )

        # Find the max profit on the last day among all transaction counts where we're not holding stock
        res = max(dp[n - 1][j][0] for j in range(k + 1))
        return res