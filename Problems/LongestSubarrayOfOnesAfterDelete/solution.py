class Solution:
    def longestSubarray(self, nums):

        max_len = 0
        zero_index = -1
        
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                left = zero_index + 1
                zero_index = right
            max_len = max(max_len, right - left)
        
        return max_len