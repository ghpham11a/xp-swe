class Solution(object):

    def combination_sum(self, candidates, target):
        output = []  # This will store all valid combinations
        # Start the backtracking process
        self.backtrack(candidates, target, [], 0, output)
        return output

    def backtrack(self, candidates, target, combination, start_index, output):
        # Base case: if target is exactly 0, we found a valid combination
        if target == 0:
            output.append(list(combination))  # Add a deep copy of current combination
            return

        # Base case: if target goes below 0, current path is invalid
        if target < 0:
            return  # Backtrack immediately

        # Iterate through candidates starting from start_index to avoid duplicates
        for i in range(start_index, len(candidates)):
            # Choose the current candidate
            combination.append(candidates[i])

            # Recurse with reduced target, allowing the same candidate again
            self.backtrack(candidates, target - candidates[i], combination, i, output)

            # Backtrack: remove last added element and try next candidate
            combination.pop()


solution = Solution()

assert(solution.combination_sum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]])

print("PASS")