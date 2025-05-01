class Solution:
    def remove_duplicates(self, nums):
        seen = set()  # To track unique values we've already encountered
        k = 0          # Pointer to place the next unique element

        # Iterate over all elements in the input array
        for i in range(len(nums)):
            # If the current element hasn't been seen before
            if nums[i] not in seen:
                nums[k] = nums[i]  # Place it at index `k`
                k += 1             # Move `k` forward for the next unique spot
                seen.add(nums[i]) # Mark this element as seen

        return k  # Return number of unique elements found
    