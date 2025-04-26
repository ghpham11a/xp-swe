class Solution:
    def product_except_self(self, nums):
        
        # Initialize the output array where each position starts as 1
        output = [1] * len(nums)

        # First pass: calculate the running product from the left side
        left_to_right = 1
        for i in range(len(nums)):
            # Set the current output[i] to the product of all numbers to the left of i
            output[i] = left_to_right
            # Update left_to_right to include nums[i] for the next position
            left_to_right *= nums[i]

        # Second pass: calculate the running product from the right side
        right_to_left = 1
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the current output[i] with the product of all numbers to the right of i
            output[i] *= right_to_left
            # Update right_to_left to include nums[i] for the next position
            right_to_left *= nums[i]

        # Final output array contains the product of all elements except nums[i] at each index
        return output

solution = Solution()

assert(solution.product_except_self([1,2,3,4]) == [24,12,8,6])

print("PASS")