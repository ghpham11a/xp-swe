from typing import List

class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []  # This will store all valid combinations

        # Helper function for backtracking
        def backtrack(start, comb):
            # If the current combination has k elements, it's complete
            if len(comb) == k:
                res.append(comb.copy())  # Add a copy to results
                return

            # Try adding each number from 'start' to 'n' into the combination
            for i in range(start, n + 1):
                comb.append(i)               # Choose number i
                backtrack(i + 1, comb)       # Explore further with i+1
                comb.pop()                   # Undo the choice (backtrack)

        # Start building combinations from number 1 with an empty list
        backtrack(1, [])
        return res