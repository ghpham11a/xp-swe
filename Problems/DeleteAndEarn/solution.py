from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Step 1: Aggregate total points for each unique number in nums.
        # We create a list where points[x] = total points earned by deleting all x's.
        max_num = max(nums)  # Find the maximum number to size our points array
        points = [0] * (max_num + 1)  # Initialize a points array from 0 to max_num

        for num in nums:
            points[num] += num  # Add num to its corresponding index to count total contribution

        # Step 2: Set up bottom-up dynamic programming (similar to House Robber problem)
        dp = [0] * (max_num + 1)  # dp[i] = max points that can be earned using numbers up to i

        dp[0] = 0               # Base case: no points for using numbers up to 0
        dp[1] = points[1]       # Base case: only points earned from using number 1

        # Step 3: Build the dp array from 2 up to max_num
        for i in range(2, max_num + 1):
            # Two choices:
            # 1. Skip number i → take dp[i - 1]
            # 2. Take number i → add points[i] + dp[i - 2] (since i-1 gets deleted)
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])

        # Step 4: Return the result which is the max points we can earn using all numbers
        return dp[max_num]