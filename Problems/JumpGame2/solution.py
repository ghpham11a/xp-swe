class Solution:

    def jump(self, nums):
        
        output = 0
        target_index = len(nums) - 1
        left = 0
        right = 0

        while right < target_index:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            output += 1
            
        return output

solution = Solution()

assert(solution.insert([2,3,1,1,4]) == 2)

print("PASS")