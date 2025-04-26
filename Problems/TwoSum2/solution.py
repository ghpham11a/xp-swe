class Solution(object):

    def two_sum(self, numbers, target):
        
        # Initialize two pointers:
        # 'left' starts from the beginning of the array
        # 'right' starts from the end of the array
        left, right = 0, len(numbers) - 1

        # Continue searching while left pointer is to the left of right pointer
        while left < right:

            # Calculate the sum of the two pointed elements
            two_sum = numbers[left] + numbers[right]

            # If the sum is greater than the target, move the right pointer leftward
            # (since the array is sorted, moving left decreases the value)
            if two_sum > target:
                right -= 1

            # If the sum is less than the target, move the left pointer rightward
            # (since moving right increases the value)
            elif two_sum < target:
                left += 1

            # If the sum matches the target, return the 1-based indices
            else:
                return [left + 1, right + 1]

solution = Solution()

assert(solution.two_sum([2,7,11,15], 9) == [1,2])

print("PASS")