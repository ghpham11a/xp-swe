class Solution:

    def subsets(self, nums):
        output = []  # This will hold all subsets generated
        self.backtrack(nums, output, [], 0)  # Start backtracking from index 0
        return output  # Return the final list of subsets

    def backtrack(self, nums, output, sub_output, i):
        # Base case: if we've considered all elements
        if i >= len(nums):
            output.append(list(sub_output))  # Add a copy of the current subset
            return

        # Choice 1: include nums[i] in the current subset
        sub_output.append(nums[i])
        self.backtrack(nums, output, sub_output, i + 1)  # Recurse with nums[i] included

        # Backtrack: remove the last element before exploring the next option
        sub_output.pop()

        # Choice 2: exclude nums[i] and move to the next
        self.backtrack(nums, output, sub_output, i + 1)  # Recurse without nums[i]

solution = Solution()

assert(solution.subsets([1,2,3]) == [[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]])

print("PASS")
