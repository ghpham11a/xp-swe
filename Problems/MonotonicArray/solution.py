class Solution:

    def is_monotonic(self, nums):

        is_increasing = True
        is_decreasing = True

        for i in range(len(nums) - 1):
            
            if is_increasing and not (nums[i] <= nums[i + 1]):
                is_increasing = False

            if is_decreasing and not (nums[i] >= nums[i + 1]):
                is_decreasing = False

        return is_increasing or is_decreasing

solution = Solution()

assert(solution.is_monotonic([1,2,2,3]) == True)

print("PASS")