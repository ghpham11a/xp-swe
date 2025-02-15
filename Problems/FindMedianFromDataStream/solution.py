import heapq

class MedianFinder(object):

    def __init__(self):
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num):
        heapq.heappush(self.small_heap, -1 * num)

        # make sure every num samll is <= every num in large
        if (self.small_heap and self.large_heap and (-1 * self.small_heap[0]) > self.large_heap[0]):
            val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)

        # uneven size?
        if len(self.small_heap) > len(self.large_heap) + 1:
            val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)

        if len(self.large_heap) > len(self.small_heap) + 1:
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -1 * val)

    def findMedian(self):
        if len(self.small_heap) > len(self.large_heap):
            return -1 * self.small_heap[0]
        if len(self.large_heap) > len(self.small_heap):
            return self.large_heap[0]

        return (-1 * self.small_heap[0] + self.large_heap[0]) / 2.0
        

class Solution(object):

    def __init__(self):
        self.median_finder = MedianFinder()

    def run(self, operations, params):

        result = []

        for index, operation in enumerate(operations):
            if operation == "MedianFinder":
                result.append(None)

            if operation == "addNum":
                self.median_finder.addNum(params[index][0])
                result.append(None)

            if operation == "findMedian":
                result.append(self.median_finder.findMedian())

        return result

runner = Solution()

assert(runner.run(["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"], [[],[1],[2],[],[3],[]]) == [None,None,None,1.50000,None,2.00000])

print("PASS")