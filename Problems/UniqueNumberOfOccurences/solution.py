from collections import defaultdict

class Solution:
    
    def unique_occurrences(self, arr):
        seen = defaultdict(int)

        for num in arr:
            seen[num] += 1

        occur = list(seen.values())
        return len(occur) == len(set(occur))