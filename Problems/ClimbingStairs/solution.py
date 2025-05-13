class Solution:

    def climb_stairs(self, n: int) -> int:

        # Base case: if there's only 1 step, there's only one way to climb it
        if n == 1:
            return 1
        
        # Create a DP array where dp[i] represents the number of ways to reach the top from step i
        dp = [0] * (n + 1)

        # There's exactly 1 way to climb from step n (you're already at the top)
        dp[n] = 1
        # There's also 1 way to climb from step n-1 (just take 1 step to the top)
        dp[n - 1] = 1

        # Fill the DP table backwards from step n-2 down to 0
        for i in range(len(dp) - 3, -1, -1):
            # Number of ways to reach the top from step i is the sum of:
            # - ways from the next step (i + 1)
            # - ways from skipping a step (i + 2)
            dp[i] = dp[i + 1] + dp[i + 2]

        # Return the number of ways from the ground level (step 0)
        return dp[0]