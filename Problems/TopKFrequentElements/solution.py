import heapq
from collections import Counter

class Solution:
    
    def top_k_frequent(self, nums, k):

        if k == len(nums):
            return nums

        counter = Counter(nums)

        return heapq.nlargest(k, counter.keys(), key = counter.get)
    
solution = Solution()

assert(solution.top_k_frequent([1,1,1,2,2,3], 2) == [1,2])

print("PASS")