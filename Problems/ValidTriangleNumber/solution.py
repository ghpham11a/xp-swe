class Solution:

    def triangle_number(self, nums):
        
        # Sort the array so we can apply the triangle inequality efficiently
        nums.sort()

        count = 0  # This will keep track of the number of valid triangle triplets

        # Start from the last element and work backwards
        # We treat nums[i] as the longest side of the triangle
        for i in range(len(nums) - 1, 1, -1):
            left = 0             # Start of the array
            right = i - 1        # Just before the current longest side

            # Use two-pointer technique to find valid pairs (nums[left], nums[right])
            while left < right:
                # If the sum of the two smaller sides is greater than the largest side,
                # then all elements between left and right form a valid triangle with nums[i]
                if nums[left] + nums[right] > nums[i]:
                    count += right - left  # All elements from left to right-1 form valid triangles
                    right -= 1             # Try a smaller second side to find more combinations
                else:
                    left += 1              # Increase the smaller side to try and satisfy the inequality

        return count  # Return the total number of valid triangle combinations