class Solution(object):

    def combination_sum_3(self, k, n):

        CANDIDATES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        output = []

        self.backtrack(0, n, k, CANDIDATES, output, [])

        return output
    
    def backtrack(self, start_index, target, limit, candidates, output, combination):

        if target == 0 and len(combination) == limit:
            output.append(list(combination))
            return

        if target < 0:
            return
        
        for i in range(start_index, len(candidates)):

            if i > start_index and candidates[i] == candidates[i - 1]:
                continue

            combination.append(candidates[i])
            self.backtrack(i + 1, target - candidates[i], limit, candidates, output, combination)
            combination.pop()

solution = Solution()

assert(solution.combination_sum_3(3, 7) == [[1,2,4]])
assert(solution.combination_sum_3(3, 9) == [[1,2,6],[1,3,5],[2,3,4]])

print("PASS")