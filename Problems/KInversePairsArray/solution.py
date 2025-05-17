class Solution:

    def k_inverse_pairs(self, n, k):
        MOD = 10**9 + 7  # Use modulo to handle large results as per problem requirement

        # prev will store the number of permutations of size N-1 with exactly K inverse pairs
        prev = [0] * (k + 1)
        prev[0] = 1  # Base case: There is exactly 1 array of size 1 with 0 inverse pairs: [1]

        # Loop over sizes of array from 1 to n
        for N in range(1, n + 1):
            # cur will store results for current N
            cur = [0] * (k + 1)
            total = 0  # This will help us compute prefix sums for optimization
            
            # Compute number of arrays of size N with K inverse pairs
            for K in range(0, k + 1):
                if K >= N:
                    # Subtract value that is now outside the window of size N
                    total -= prev[K - N]
                
                # Add current prefix sum value
                total = (total + prev[K]) % MOD

                # Store the result for current N and K
                cur[K] = total
            
            # Move current result to prev for the next iteration
            prev = cur

        # Return result for size n and exactly k inverse pairs
        return prev[k]

solution = Solution()

assert(solution.k_inverse_pairs(3, 0) == 1)
assert(solution.k_inverse_pairs(3, 1) == 2)

print("PASS")