class Solution:
    def product_except_self(self, nums):
        
        output = [1] * len(nums)

        left_to_right = 1
        for i in range(len(nums)):
            output[i] = left_to_right
            left_to_right *= nums[i]

        right_to_left = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *= right_to_left
            right_to_left *= nums[i]

        return output

solution = Solution()

assert(solution.product_except_self([1,2,3,4]) == [24,12,8,6])

print("PASS")