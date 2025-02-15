class Solution:

    def permute_unique(self, nums):
        output = []

        counts = { n:0 for n in nums }
        for n in nums:
            counts[n] += 1

        self.backtrack(nums, [], output, counts)
        return output

    def backtrack(self, nums, sub_output, output, counts):
        if len(sub_output) == len(nums):
            output.append(list(sub_output))
            return

        for num in counts:
            if counts[num] > 0:
                sub_output.append(num)
                counts[num] -= 1

                self.backtrack(nums, sub_output, output, counts)

                sub_output.pop()
                counts[num] += 1

solution = Solution()

assert(solution.permute_unique([1,1,2]) == [[1,1,2],[1,2,1],[2,1,1]])

print("PASS")