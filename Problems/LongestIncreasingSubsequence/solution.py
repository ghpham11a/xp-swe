class Solution(object):

    def length_of_lis(self, nums):
        table = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    table[i] = max(table[i], table[j] + 1)

        return max(table)

solution = Solution()

assert(solution.length_of_lis([10,9,2,5,3,7,101,18]) == 4)

print("PASS")