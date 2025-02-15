class Solution:

    def subsets_with_dup(self, nums):
        nums.sort()
        output = []
        self.backtrack(nums, output, [], 0)
        return output

    def backtrack(self, nums, output, sub_output, index):

        if index >= len(nums):
            output.append(list(sub_output))
            return

        sub_output.append(nums[index])
        self.backtrack(nums, output, sub_output, index + 1)
        sub_output.pop()

        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        
        self.backtrack(nums, output, sub_output, index + 1)

solution = Solution()

assert(solution.subsets_with_dup([1,2,2]) == [[1,2,2],[1,2],[1],[2,2],[2],[]])

print("PASS")