class Solution:

    def rob_helper(self, nums):

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for home_index in range(2, len(nums)):
            dp[home_index] = max(nums[home_index] + dp[home_index - 2], dp[home_index - 1])

        return dp[-1]

    def rob(self, nums):
        
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))

solution = Solution()

assert(solution.rob([1,2,3,1]) == 4)

print("PASS")