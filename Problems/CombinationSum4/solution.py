from typing import List

class Solution(object):

    def combination_sum_4(self, nums: List[int], target: int) -> int:
        # Initialize a DP table where table[i] will store the number of ways to get sum i
        table = [0 for i in range(target + 1)]

        # Base case: There's exactly 1 way to make sum 0 (by choosing no elements)
        table[0] = 1

        # Iterate through all possible intermediate target sums
        for comb_sum in range(target + 1):
            # Try each number in the input list
            for num in nums:
                # If the current number can contribute to the current sum
                if comb_sum - num >= 0:
                    # Add the number of ways to make (comb_sum - num) to the current sum
                    table[comb_sum] += table[comb_sum - num]

        # The answer is the number of ways to make the full target sum
        return table[-1]

solution = Solution()

assert(solution.combination_sum_3([1,2,3], 4) == 7)

print("PASS")