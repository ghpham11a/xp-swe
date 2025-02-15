class Solution:
    def k_sum(self, nums, target, k):
        output = []
        
        if not nums:
            return output
        
        if k == 2:
            return self.two_sum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for subset in self.k_sum(nums[i + 1:], target - nums[i], k - 1):
                    output.append([nums[i]] + subset)

        return output

    def two_sum(self, nums, target):
        output = []
        lo, hi = 0, len(nums) - 1

        while (lo < hi):
            curr_sum = nums[lo] + nums[hi]
            if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                output.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                                                        
        return output

    def four_sum(self, nums, target):
        nums.sort()
        return self.k_sum(nums, target, 4)

runner = Solution()

assert(runner.four_sum([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])

print("PASS")