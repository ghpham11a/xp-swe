class Solution(object):
    
    def combination_sum_2(self, candidates, target):
        # Sort candidates to handle duplicates and allow early pruning
        candidates.sort()
        
        output = []  # Stores all unique valid combinations
        
        # Begin backtracking from index 0 with an empty combination
        self.backtrack(0, target, candidates, output, [])
        
        return output
    
    def backtrack(self, start_index, target, candidates, output, combination):
        # If the target is reached exactly, we found a valid combination
        if target == 0:
            output.append(list(combination))  # Make a copy and store it
            return

        # If target goes negative, stop exploring this path (invalid)
        if target < 0:
            return
        
        # Iterate over the candidates starting from the given index
        for i in range(start_index, len(candidates)):
            # Skip duplicates: only consider the first occurrence at this level
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue

            # Choose the current candidate
            combination.append(candidates[i])
            
            # Recurse with remaining target and move to the next index (i + 1)
            self.backtrack(i + 1, target - candidates[i], candidates, output, combination)
            
            # Backtrack: remove the last added candidate to try the next possibility
            combination.pop()

solution = Solution()

assert(solution.combination_sum_2([10,1,2,7,6,1,5], 8) == [[1,1,6],[1,2,5],[1,7],[2,6]])

print("PASS")