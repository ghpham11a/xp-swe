class Solution(object):

    def find_peak_element(self, nums):
        
        # Initialize binary search bounds
        start = 0
        end = len(nums) - 1

        # Binary search loop: continue until the search space is narrowed to one element
        while start < end:
            # Calculate middle index to avoid overflow
            middle = start + (end - start) // 2

            # Compare middle element with its right neighbor
            if nums[middle] < nums[middle + 1]:
                # Ascending slope: a peak must exist on the right side
                # Move the start pointer to the right half (excluding middle)
                start = middle + 1
            else:
                # Descending slope or local peak: a peak is on the left side (could include middle)
                # Move the end pointer to the left half (including middle)
                end = middle

        # When start == end, we found a peak (could be any valid one)
        return start