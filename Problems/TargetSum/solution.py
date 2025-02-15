class Solution:

    def find_target_sum_ways(self, nums, target):
        cache = {}

        return self.backtrack(nums, cache, target, 0, 0)

    def backtrack(self, nums, cache, target, i, total):
        if i == len(nums):
            return 1 if total == target else 0

        if (i, total) in cache:
            return cache[(i, total)]

        add_result = self.backtrack(nums, cache, target, i + 1, total + nums[i])
        subtract_result = self.backtrack(nums, cache, target, i + 1, total - nums[i])

        cache[(i, total)] = add_result + subtract_result

        return cache[(i, total)]