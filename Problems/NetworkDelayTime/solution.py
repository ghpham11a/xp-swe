from collections import defaultdict
import heapq 

class Solution(object):

    def network_delay_time(self, times, n , k):
        
        graph = defaultdict(list)
        for src, dst, weight in times:
            graph[src].append((dst, weight))

        pq = [(0, k)]
        visited = set()
        result = 0

        while pq:
            src_weight, src = heapq.heappop(pq)
            if src in visited:
                continue

            visited.add(src)
            result = max(result, src_weight)

            for dst, dst_weight in graph[src]:
                if dst not in visited:
                    heapq.heappush(pq, (src_weight + dst_weight, dst))

        return result if len(visited) == n else -1

runner = Solution()

assert(runner.network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2)
assert(runner.network_delay_time([[1,2,1]], 2, 1) == 1)
assert(runner.network_delay_time([[1,2,1]], 2, 2) == -1)

print("PASS")

        