class Solution:

    def subsets_with_dup(self, nums):
        nums.sort()  # Sort the array to group duplicates together
        output = []  # This will store the final list of unique subsets
        self.backtrack(nums, output, [], 0)  # Start backtracking from index 0
        return output  # Return the final result

    def backtrack(self, nums, output, sub_output, index):
        # Base case: if index goes beyond the last element, record the current subset
        if index >= len(nums):
            output.append(list(sub_output))  # Append a copy of the current subset
            return

        # Choice 1: include the current number
        sub_output.append(nums[index])
        self.backtrack(nums, output, sub_output, index + 1)  # Recurse with current number
        sub_output.pop()  # Backtrack: remove the last added number

        # Skip over duplicates
        # If the next number is the same as the current one, skip all its copies
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        
        # Choice 2: exclude the current number and move to the next distinct number
        self.backtrack(nums, output, sub_output, index + 1)

solution = Solution()

assert(solution.subsets_with_dup([1,2,2]) == [[1,2,2],[1,2],[1],[2,2],[2],[]])

print("PASS")