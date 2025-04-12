class Solution:

    def max_frequency(self, nums, k):
        # Sort the array so that the numbers are in non-decreasing order.
        # This is important because once sorted, if we want to make a group of numbers equal,
        # making them all equal to the largest number in the group (nums[right]) minimizes the cost.
        nums.sort()

        # Initialize two pointers for the sliding window.
        # 'left' is the start index of the window and 'right' is the end index.
        left, right = 0, 0

        # 'output' will store the maximum frequency (window size) found.
        # 'total' will keep track of the sum of the elements in the current window.
        output, total = 0, 0

        # Iterate over the array with the 'right' pointer acting as the end of the window.
        while right < len(nums):
            # Add the current element to the total sum of the window.
            total += nums[right]

            # Calculate if we can make all elements in the window equal to nums[right]
            # with at most k increments.
            # The required operations to convert all elements in the window to nums[right] is:
            #   (nums[right] * window_size) - total
            # If this number exceeds k, we cannot include all elements in this window.
            while nums[right] * (right - left + 1) > total + k:
                # Remove the element at the start of the window from the total,
                # because we are going to shrink the window from the left.
                total -= nums[left]
                # Move the left pointer to the right to shrink the window.
                left += 1

            # Update the output with the size of the current window if it's larger than previous windows.
            output = max(output, right - left + 1)
            # Expand the window by moving the right pointer to the next element.
            right += 1

        # Return the maximum frequency of an element after at most k operations.
        return output
    
solution = Solution()

assert(solution.max_frequency([1,4,8,13], 5) == 2)

print("PASS")