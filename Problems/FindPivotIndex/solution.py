from typing import List

class Solution(object):
    def pivot_index(self, nums: List[int]) -> int:
        # Compute the total sum of the array
        total_sum = sum(nums)

        # Initialize left_sum to 0 since there are no elements to the left initially
        left_sum = 0

        # Iterate through the array with index and value
        for i, num in enumerate(nums):
            # Check if current index is a pivot index:
            # left_sum is the sum of elements to the left of index i
            # total_sum - left_sum - num is the sum of elements to the right of index i
            if left_sum == (total_sum - left_sum - num):
                return i  # Found the pivot index, return it immediately

            # Update left_sum to include the current number
            left_sum += num

        # If no pivot index is found, return -1
        return -1