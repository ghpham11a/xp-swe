class Solution:

    def k_inverse_pairs(self, n, k):
        MOD = 10**9 + 7

        prev = [0] * (k + 1)
        prev[0] = 1

        for N in range(1, n + 1):
            cur = [0] * (k + 1)
            total = 0
            for K in range(0, k + 1):
                if K >= N:
                    total -= prev[K - N]
                total = (total + prev[K]) % MOD
                cur[K] = total
            prev = cur
        return prev[k]

solution = Solution()

assert(solution.k_inverse_pairs(3, 0) == 1)
assert(solution.k_inverse_pairs(3, 1) == 2)

print("PASS")