class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Stack will store pairs [nums[j], min_i] where:
        # - nums[j] is a candidate for the '3' in the 132 pattern
        # - min_i is the smallest number before nums[j], a candidate for '1'
        # The stack is maintained in decreasing order of nums[j]
        stack = []

        # This keeps track of the minimum value seen so far (i.e., min_i)
        cur_min = float("inf")

        # Iterate through the array starting from the first element
        for n in nums:
            # Maintain decreasing stack: pop any elements whose nums[j] <= current value
            # Because if n >= nums[j], then nums[j] can't be the '3' in a valid 132 pattern
            while stack and n >= stack[-1][0]:
                stack.pop()

            # Now check if current number 'n' (candidate for nums[k]) is greater than min_i
            # of the last pair in the stack. If yes, we found nums[i] < nums[k] < nums[j]
            if stack and n > stack[-1][1]:
                return True

            # Append the current number as a new candidate for nums[j], along with the min so far
            stack.append([n , cur_min])

            # Update the current minimum seen so far (candidate for nums[i])
            cur_min = min(cur_min, n)

        # If no valid pattern found after full iteration
        return False