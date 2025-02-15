class Solution(object):

    def combination_sum(self, candidates, target):

        output = []

        self.backtrack(candidates, target, [], 0, output)

        return output

    def backtrack(self, candidates, target, combination, start_index, output):

        if target == 0:
            output.append(list(combination))
            return

        if target < 0:
            return

        for i in range(start_index, len(candidates)):

            combination.append(candidates[i])

            self.backtrack(candidates, target - candidates[i], combination, i, output)

            combination.pop()

solution = Solution()

assert(solution.combination_sum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]])

print("PASS")