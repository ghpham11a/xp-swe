from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # This set will store the sliding window of up to 'k' most recent elements
        window = set()

        # Left pointer of the sliding window
        left = 0

        # Iterate through the array with the right pointer
        for right in range(len(nums)):

            # Ensure the sliding window size does not exceed 'k'
            if right - left > k:
                # Remove the leftmost element as it's now out of the window range
                window.remove(nums[left])
                left += 1

            # If the current number is already in the window,
            # it means we found a duplicate within range 'k'
            if nums[right] in window:
                return True

            # Add the current number to the sliding window
            window.add(nums[right])

        # If we finish the loop without finding any duplicates in range 'k'
        return False