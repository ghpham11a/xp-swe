class Solution:

    def rob_helper(self, nums):
        # rob_helper solves the original House Robber problem (linear version)
        dp = [0] * len(nums)

        # Base case: only one house
        dp[0] = nums[0]

        # Base case: pick the richer of the first two houses
        dp[1] = max(nums[0], nums[1])

        # Iterate through the remaining houses
        for home_index in range(2, len(nums)):
            # Decide whether to rob current house and add its value to dp[i-2]
            # or skip it and take the previous max dp[i-1]
            dp[home_index] = max(nums[home_index] + dp[home_index - 2], dp[home_index - 1])

        # Return the max money robable from this linear segment
        return dp[-1]

    def rob(self, nums):
        # Edge case: no houses
        if len(nums) == 0:
            return 0

        # Edge case: only one house
        if len(nums) == 1:
            return nums[0]

        # Edge case: only two houses, pick the richer one
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Main logic: choose the best of two scenarios
        # 1. Rob houses from index 1 to end (exclude first)
        # 2. Rob houses from index 0 to second-last (exclude last)
        # This avoids robbing both first and last (which are neighbors)
        return max(self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))

solution = Solution()

assert(solution.rob([1,2,3,1]) == 4)

print("PASS")