class Solution:

    def sort_colors(self, nums):
       
        # Initialize three pointers:
        # 'left' will track the boundary of where 0s should go.
        # 'right' will track the boundary of where 2s should go.
        # 'curr' will traverse through the array.
        left = 0
        curr = 0
        right = len(nums) - 1

        # Continue the loop until 'curr' passes 'right'
        while curr <= right:
            # If the current number is 0, swap it to the 'left' side
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1  # move forward since the swapped-in element is already processed

            # If the current number is 2, swap it to the 'right' side
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
                # Do not increment 'curr' here because the swapped-in value needs to be evaluated

            # If the current number is 1, just move to the next
            else:
                curr += 1

solution = Solution()

assert(solution.sort_colors([2,0,2,1,1,0]) == [0,0,1,1,2,2])

print("PASS")