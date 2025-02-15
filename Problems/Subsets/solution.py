class Solution:

    def subsets(self, nums):
        output = []
        self.backtrack(nums, output, [], 0)
        return output

    def backtrack(self, nums, output, sub_output, i):

        if i >= len(nums):
            output.append(list(sub_output))
            return

        sub_output.append(nums[i])
        self.backtrack(nums, output, sub_output, i + 1)

        sub_output.pop()
        self.backtrack(nums, output, sub_output, i + 1)

solution = Solution()

assert(solution.subsets([1,2,3]) == [[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]])

print("PASS")
