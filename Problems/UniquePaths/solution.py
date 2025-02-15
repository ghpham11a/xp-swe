class Solution:

    def unique_paths(self, m, n):
        
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]

solution = Solution()

assert(solution.unique_paths(3, 7) == 28)

print("PASS")