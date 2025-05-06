from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Pointer to track the position to place the next non-zero element
        left = 0

        # Iterate through each element with the 'right' pointer
        for right in range(len(nums)):
            # If the current element is non-zero
            if nums[right]:
                # Swap the non-zero element at 'right' with the element at 'left'
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

                # Move the 'left' pointer forward to the next position
                left += 1