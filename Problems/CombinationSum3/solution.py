class Solution(object):

    def combination_sum_3(self, k, n):
        # Define the candidate numbers from 1 to 9
        CANDIDATES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        output = []  # This will store all valid combinations

        # Start backtracking from index 0 with an empty combination
        self.backtrack(0, n, k, CANDIDATES, output, [])

        return output
    
    def backtrack(self, start_index, target, limit, candidates, output, combination):
        # Base case: valid combination found
        if target == 0 and len(combination) == limit:
            output.append(list(combination))  # Add a copy of the current combination
            return

        # If the remaining target is negative, prune this path
        if target < 0:
            return
        
        # Explore all candidates starting from current index
        for i in range(start_index, len(candidates)):

            # Optional: skip duplicates (not strictly needed since candidates are unique)
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue

            # Choose the current number
            combination.append(candidates[i])

            # Recurse: move to the next index, reduce the target
            self.backtrack(i + 1, target - candidates[i], limit, candidates, output, combination)

            # Backtrack: remove the last number to try other paths
            combination.pop()

solution = Solution()

assert(solution.combination_sum_3(3, 7) == [[1,2,4]])
assert(solution.combination_sum_3(3, 9) == [[1,2,6],[1,3,5],[2,3,4]])

print("PASS")