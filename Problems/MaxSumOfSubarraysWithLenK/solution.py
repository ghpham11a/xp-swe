from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        output = 0  # Holds the maximum valid subarray sum found

        count = defaultdict(int)  # Tracks the frequency of elements in the current window
        cur_sum = 0  # Running sum of the current window

        l = 0  # Left pointer of the sliding window
        for r in range(len(nums)):  # Right pointer moves through the array
            cur_sum += nums[r]  # Add the new element to the current window sum
            count[nums[r]] += 1  # Update the frequency count of nums[r]

            # If window size exceeds k, shrink it from the left
            if r - l + 1 > k:
                count[nums[l]] -= 1  # Decrease frequency of the element being removed
                if count[nums[l]] == 0:  # Clean up the dictionary to maintain accurate distinct count
                    del count[nums[l]]
                cur_sum -= nums[l]  # Subtract the removed element from the sum
                l += 1  # Move left pointer forward

            # Check if the window is of size k and all elements are distinct
            if len(count) == k and r - l + 1 == k:
                output = max(output, cur_sum)  # Update max sum if current window is valid

        return output  # Return the highest valid subarray sum found