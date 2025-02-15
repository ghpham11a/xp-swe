import heapq

class Solution(object):

    def max_performance(self, n, speed, efficiency, k):
        
        table = list(zip(efficiency, speed))
        table.sort(reverse=True)

        result = 0
        speed = 0
        min_heap = []
        for eff, spd in table:
            if len(min_heap) == k:
                speed -= heapq.heappop(min_heap)
            speed += spd
            heapq.heappush(min_heap, spd)
            result = max(result, eff * speed)

        return result % (10 ** 9 + 7)

solution = Solution()

assert(solution.max_performance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2) == 60)

print("PASS")