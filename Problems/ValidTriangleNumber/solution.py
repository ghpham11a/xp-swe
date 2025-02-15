class Solution:

    def triangle_number(self, nums):
        
        count = 0
        nums.sort()
        
        for small_side in range(len(nums) - 2):

            # If the first element of the triplet is 0, move to the next element
            if nums[small_side] == 0:
                continue

            # Initialize third pointer to i + 2
            large_side = small_side + 2

            # Loop through all possible second elements of the triplet
            for other_side in range(small_side + 1, len(nums) - 1):

                # Move the third pointer to the first element that is greater than or equal to the sum of the first two elements
                while large_side < len(nums) and nums[small_side] + nums[other_side] > nums[large_side]:
                    large_side += 1

                # The number of valid triangles that can be formed with the current pair of first two elements is the difference between the third pointer and the second pointer minus 1
                count += (large_side - other_side - 1)
                    
        return count