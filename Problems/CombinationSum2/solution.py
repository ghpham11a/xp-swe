class Solution(object):
    
    def combination_sum_2(self, candidates, target):

        candidates.sort()
        output = []
        self.backtrack(0, target, candidates, output, [])

        return output
    
    def backtrack(self, start_index, target, candidates, output, combination):

        if target == 0:
            output.append(list(combination))
            return

        if target < 0:
            return
        
        for i in range(start_index, len(candidates)):

            if i > start_index and candidates[i] == candidates[i - 1]:
                continue

            combination.append(candidates[i])
            self.backtrack(i + 1, target - candidates[i], candidates, output, combination)
            combination.pop()

solution = Solution()

assert(solution.combination_sum_2([10,1,2,7,6,1,5], 8) == [[1,1,6],[1,2,5],[1,7],[2,6]])

print("PASS")