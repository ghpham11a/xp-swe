class Solution(object):

    def combination_sum_4(self, nums: List[int], target: int) -> int:

        table = [0 for i in range(target + 1)]
        table[0] = 1

        for comb_sum in range(target + 1):
            for num in nums:
                if comb_sum - num >= 0:
                    table[comb_sum] += table[comb_sum - num]

        return table[-1]

solution = Solution()

assert(solution.combination_sum_3([1,2,3], 4) == 7)

print("PASS")