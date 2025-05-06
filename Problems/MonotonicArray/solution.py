class Solution:

    def is_monotonic(self, nums):

        # Initialize flags to track whether the array is increasing or decreasing
        is_increasing = True
        is_decreasing = True

        # Iterate through the array, comparing adjacent elements
        for i in range(len(nums) - 1):

            # If we ever find nums[i] > nums[i+1], it's not increasing
            if is_increasing and not (nums[i] <= nums[i + 1]):
                is_increasing = False

            # If we ever find nums[i] < nums[i+1], it's not decreasing
            if is_decreasing and not (nums[i] >= nums[i + 1]):
                is_decreasing = False

        # The array is monotonic if it is either entirely non-increasing or non-decreasing
        return is_increasing or is_decreasing

solution = Solution()

assert(solution.is_monotonic([1,2,2,3]) == True)

print("PASS")