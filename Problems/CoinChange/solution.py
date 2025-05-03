from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the dp array where dp[i] will store the minimum number of coins needed for amount i.
        # We start by filling the array with infinity to represent unreachable states.
        dp = [float("inf")] * (amount + 1)
        
        # Base case: it takes 0 coins to make up amount 0
        dp[0] = 0

        # Loop through each coin denomination
        for coin in coins:
            # For each amount from coin to amount, update the dp table
            for i in range(coin, amount + 1):
                # We try to take this coin and see if it results in a lesser number of coins
                # dp[i - coin] gives the minimum coins needed for the (i - coin) amount
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # If the amount is still infinity, it means we can't make the amount with given coins
        return dp[amount] if dp[amount] != float("inf") else -1