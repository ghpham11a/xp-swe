class Solution:
    
    def find_max_average(self, nums, k):
        cur_sum = max_sum = sum(nums[:k])

        for i in range(len(nums) - k):
            cur_sum -= nums[i]
            cur_sum += nums[i + k]
            max_sum = max(max_sum, cur_sum)

        return max_sum / k