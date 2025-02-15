import collections

class Solution(object):

    def max_sliding_window(self, nums, k):

        deque = collections.deque()

        output = []

        for index in range(k):
            while deque and nums[index] >= nums[deque[-1]]:
                deque.pop()
            deque.append(index)

        output.append(nums[deque[0]])

        for index in range(k, len(nums)):
            if deque and deque[0] == index - k:
                deque.popleft()
            while deque and nums[index] >= nums[deque[-1]]:
                deque.pop()

            deque.append(index)
            output.append(nums[deque[0]])

        return output
            
solution = Solution()

assert(solution.max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7])

print("PASS")