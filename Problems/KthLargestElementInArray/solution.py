import heapq

class Solution(object):

    def find_kth_largest(self, nums, k):

         # Initialize an empty list to use as a max heap.
        # Since Python's heapq module only supports a min heap,
        # we simulate a max heap by pushing negative numbers.
        max_heap = []

        # Push the negative of each number into the heap
        for num in nums:
            heapq.heappush(max_heap, -1 * num)  # Push -num to simulate max-heap behavior

        output = 0
        # Pop from the heap k times to get the kth largest element
        for n in range(k):
            output = heapq.heappop(max_heap)  # Remove the largest remaining element (smallest negative)

        # Convert back to positive before returning
        return output * -1

solution = Solution()

assert(solution.combination_sum_3([3,2,1,5,6,4], 2) == 5)

print("PASS")