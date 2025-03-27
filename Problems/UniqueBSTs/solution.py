class Solution:

    def num_trees(self, n: int) -> int:

        dp = [0] * (n + 1)

        dp[0], dp[1] = 1, 1

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += dp[left] * dp[right]
            dp[nodes] = total
        return dp[n]
    
solution = Solution()

assert(solution.num_trees(3) == 5)

print("PASS")