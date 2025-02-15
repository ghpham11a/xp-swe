class Solution(object):

    def permute(self, nums):
        output = []
        self.backtrack(nums, [], output)
        return output

    def backtrack(self, nums, sub_output, output):
        if len(sub_output) == len(nums):
            output.append(list(sub_output))
            return
        
        for num in nums:
            if num not in sub_output:
                sub_output.append(num)
                self.backtrack(nums, sub_output, output)
                sub_output.pop()

solution = Solution()

assert(solution.max_profit([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

print("PASS")