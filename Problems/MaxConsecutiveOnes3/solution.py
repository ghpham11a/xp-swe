from typing import List

class Solution:
    def longest_ones(self, nums: List[int], k: int) -> int:
        
        # Initialize the maximum width of the sliding window
        max_width = float("-inf")
        # Counter to track how many 0s are in the current window
        num_zeroes = 0

        # Left pointer for the sliding window
        left = 0
        
        # Iterate with the right pointer through the entire array
        for right in range(len(nums)):
            
            # If we encounter a 0, we consider flipping it and increment the counter
            if nums[right] == 0:
                num_zeroes += 1

            # If number of 0s exceeds k, move the left pointer to shrink the window
            # until we are back to at most k flipped 0s
            while num_zeroes > k:
                if nums[left] == 0:
                    num_zeroes -= 1  # Unflip this 0 as it exits the window
                left += 1  # Shrink the window from the left

            # Update the maximum width of the valid window
            max_width = max(max_width, right - left + 1)

        return max_width