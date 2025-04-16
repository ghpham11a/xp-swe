from collections import defaultdict

class Solution:
    
    def max_operations(self, nums, k):
        seen = defaultdict(int)
        output = 0

        for num in nums:

            if seen[k - num] > 0:
                output += 1
                seen[k - num] -= 1
            else:
                seen[num] += 1

        return output