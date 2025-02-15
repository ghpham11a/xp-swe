class Solution:

    def can_jump(self, nums):
        
        target = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= target:
                target = i

        return target == 0


solution = Solution()

assert(solution.insert([2,3,1,1,4]) == True)

print("PASS")