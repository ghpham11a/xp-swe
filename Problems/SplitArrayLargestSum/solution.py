from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # The lowest possible value for the largest subarray sum is the maximum element (since we can't split an element)
        # The highest possible value is the sum of all elements (no split at all)
        low, high, ans = max(nums), sum(nums), -1

        # Binary search between the low and high bounds to find the minimal largest subarray sum
        while low <= high:
            mid = low + (high - low) // 2  # Try mid as a candidate for the maximum subarray sum
            if self.is_valid(nums, k, mid): 
                # If it is possible to split the array into at most k parts with max subarray sum <= mid
                ans = mid       # mid is a valid answer, but we try to find a smaller one
                high = mid - 1  # search left side for smaller possible max sum
            else:
                low = mid + 1   # Otherwise, we need a larger max subarray sum
        return ans

    def is_valid(self, nums, m, mid):
        # Helper function to check if we can split `nums` into at most `m` subarrays
        # such that the sum of each subarray is <= mid
        cuts, curr_sum  = 0, 0  # Start with 0 cuts and 0 current sum
        for x in nums:
            curr_sum += x
            if curr_sum > mid:
                # If adding x exceeds mid, we must start a new subarray (make a cut here)
                cuts += 1
                curr_sum = x  # Reset curr_sum to the current number
        subs = cuts + 1  # Number of subarrays is cuts + 1
        return subs <= m  # True if we can split within m parts