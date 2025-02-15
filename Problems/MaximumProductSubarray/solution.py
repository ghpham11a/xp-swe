class Solution:

    def max_product(self, nums):
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        output = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            output = max(max_so_far, output)

        return output

solution = Solution()

assert(solution.max_sub_array([2,3,-2,4]) == 6)

print("PASS")