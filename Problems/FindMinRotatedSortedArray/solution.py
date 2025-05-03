from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize the result with the first element
        res = nums[0]

        # Set up binary search boundaries
        lo = 0
        hi = len(nums) - 1

        # Perform binary search
        while lo <= hi:
            # If the current subarray is already sorted (no rotation),
            # then the smallest element is at the beginning of this subarray
            if nums[lo] < nums[hi]:
                return min(res, nums[lo])

            # Find the middle index
            mid = (lo + hi) // 2

            # Update the result with the minimum value seen so far
            res = min(res, nums[mid])

            # Determine which half to search next
            if nums[mid] >= nums[lo]:
                # Left half is sorted, so minimum must be in the right half
                lo = mid + 1
            else:
                # Right half is unsorted, so minimum must be in the left half (including mid)
                hi = mid - 1

        # Return the minimum value found
        return res