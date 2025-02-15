import heapq

class Solution(object):

    def find_kth_largest(self, nums, k):

        max_heap = []

        for num in nums:
            heapq.heappush(max_heap, -1 * num)

        output = 0
        for n in range(k):
            output = heapq.heappop(max_heap)

        return output * -1

solution = Solution()

assert(solution.combination_sum_3([3,2,1,5,6,4], 2) == 5)

print("PASS")