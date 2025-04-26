class Solution(object):

    def three_sum(self, nums):
        
        output = []

        # Sort the array to make it easier to use two pointers and handle duplicates
        nums.sort()

        # Iterate through each number in the array
        for index, num in enumerate(nums):

            # Skip duplicate values to avoid duplicate triplets in the output
            if index > 0 and num == nums[index - 1]:
                continue

            # Initialize two pointers:
            # 'left' starts right after the current number
            # 'right' starts at the end of the array
            left, right = index + 1, len(nums) - 1

            # Use two pointers to find pairs that sum with num to zero
            while left < right:

                # Calculate the current sum of the triplet
                three_sum = num + nums[left] + nums[right]

                if three_sum > 0:
                    # If the sum is too big, move the right pointer leftward to reduce the sum
                    right -= 1
                elif three_sum < 0:
                    # If the sum is too small, move the left pointer rightward to increase the sum
                    left += 1
                else:
                    # If the sum is zero, add the triplet to the output list
                    output.append([num, nums[left], nums[right]])
                    # Move the left pointer to look for the next possible triplet
                    left += 1
                    # Skip over duplicate values to ensure each triplet is unique
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        # Return the list of unique triplets
        return output

solution = Solution()

assert(solution.three_sum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]])

print("PASS")