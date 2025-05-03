from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        # Initialize the binary search bounds
        left = 0
        right = len(nums) - 1

        # Continue searching while the search space is valid
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2

            # If the middle element is the target, return its index
            if target == nums[mid]:
                return mid

            # Check if the left half [left..mid] is sorted
            elif nums[mid] >= nums[left]:
                # If the target is within the sorted left half, search in that half
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    # Otherwise, search in the right half
                    left = mid + 1

            # Otherwise, the right half [mid..right] must be sorted
            else:
                # If the target is within the sorted right half, search in that half
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    # Otherwise, search in the left half
                    right = mid - 1

        # Target not found
        return -1