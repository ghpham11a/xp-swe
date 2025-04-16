class Solution:
    def longest_ones(self, nums, k):
        
        max_width = float("-inf")
        num_zeroes = 0

        left = 0
        for right in range(len(nums)):

            if nums[right] == 0:
                num_zeroes += 1

            while num_zeroes > k:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1

            max_width = max(max_width, right - left + 1)

        return max_width