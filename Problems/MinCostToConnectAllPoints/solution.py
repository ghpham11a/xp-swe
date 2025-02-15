import heapq 

class Solution(object):

    def min_cost_connect_points(self, points):

        num_points = len(points)

        graph = { i: [] for i in range(num_points) }

        for index in range(num_points):
            x1, y1 = points[index]
            for next_index in range(index + 1, num_points):
                x2, y2 = points[next_index]
                cost = abs(x1 - x2) + abs(y1 - y2)
                graph[index].append((cost, next_index))
                graph[next_index].append((cost, index))

        output = 0
        visited = set()
        min_heap = [(0, 0)]

        while len(visited) < num_points:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            output += cost
            visited.add(i)
            for neighbor_cost, neighbor in graph[i]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (neighbor_cost, neighbor))

        return output

solution = Solution()

assert(solution.min_cost_connect_points([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20)

print("PASS")