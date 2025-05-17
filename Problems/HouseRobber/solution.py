class Solution:
    def rob(self, nums):
        # If the list is empty, there's nothing to rob
        if not nums:
            return 0

        # If there's only one house, rob it
        if len(nums) == 1:
            return nums[0]

        # If there are two houses, rob the one with the most money
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Initialize a DP array where dp[i] represents the maximum money
        # that can be robbed from the first i+1 houses
        dp = [0] * len(nums)

        # Base cases
        dp[0] = nums[0]  # Only one house to rob
        dp[1] = max(nums[0], nums[1])  # Choose the richer of the first two houses
        
        # Iterate from the third house onward
        for home_index in range(2, len(nums)):
            # For each house, decide whether to:
            # 1. Rob it and add its value to the max from two houses before (nums[i] + dp[i-2])
            # 2. Skip it and take the max from the previous house (dp[i-1])
            dp[home_index] = max(nums[home_index] + dp[home_index - 2], dp[home_index - 1])

        # The last element in dp contains the answer for all houses
        return dp[-1]
    
solution = Solution()

assert(solution.rob([1,2,3,1]) == 4)

print("PASS")