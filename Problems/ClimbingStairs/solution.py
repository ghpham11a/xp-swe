class Solution:

    def climb_stairs(self, n: int) -> int:

        if n == 1:
            return 1
        
        dp = [0] * (n + 1)

        dp[n] = 1
        dp[n - 1] = 1

        for i in range(len(dp) - 3, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]