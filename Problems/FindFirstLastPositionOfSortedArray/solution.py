from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Perform binary search twice:
        # First to find the leftmost (first) index of the target
        left = self.binary_search(nums, target, True)
        # Then to find the rightmost (last) index of the target
        right = self.binary_search(nums, target, False)
        return [left, right]

    def binary_search(self, nums: List[int], target: int, left_bias: bool) -> int:
        left = 0
        right = len(nums) - 1
        i = -1  # Default return value if target is not found

        # Standard binary search loop
        while left <= right:
            mid = left + (right - left) // 2

            if target > nums[mid]:
                # Target must be in the right half
                left = mid + 1
            elif target < nums[mid]:
                # Target must be in the left half
                right = mid - 1
            else:
                # Found target, record index
                i = mid
                if left_bias:
                    # Continue searching left half for the first occurrence
                    right = mid - 1
                else:
                    # Continue searching right half for the last occurrence
                    left = mid + 1

        # Return the leftmost or rightmost index found, or -1 if not found
        return i