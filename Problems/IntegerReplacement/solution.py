class Solution:
    def integer_replacement(self, n):
        memo = {1:0}
        return self.recurse(n, memo)

    def recurse(self, n, memo):
        if n in memo:
            return memo[n]
        elif n % 2:
            memo[n] = 1 + min(self.recurse(n - 1, memo), self.recurse(n + 1, memo))
            return memo[n]
        else:
            memo[n] = 1 + self.recurse(n // 2, memo)
            return memo[n]
        
solution = Solution()

assert(solution.integer_replacement(8) == 3)

print("PASS")