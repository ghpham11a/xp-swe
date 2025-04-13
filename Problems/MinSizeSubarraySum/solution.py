class Solution:
    def minSubArrayLen(self, target, nums):
        # l is the left boundary of the sliding window, and total keeps the sum of the current window.
        l, total = 0, 0
        # Initialize output with infinity to represent the minimum length found.
        # If no valid subarray is found, output remains infinity.
        output = float("inf")

        # Iterate with r as the right boundary of the window (using indices from 0 to len(nums)-1)
        for r in range(len(nums)):
            # Add the current element to the total sum in the current window.
            total += nums[r]
            # While the current window has a sum >= target, try to shrink the window from the left.
            while total >= target:
                # Update output with the smaller value: either the current output or the size of the current window.
                output = min(output, r - l + 1)
                # Subtract the element at the left boundary from the total, since we're going to move l forward.
                total -= nums[l]
                # Increment the left pointer to shrink the window.
                l += 1

        # If output is still infinity, it means no subarray with sum >= target was found, so return 0.
        # Otherwise, return the minimal length found.
        return 0 if output == float("inf") else output