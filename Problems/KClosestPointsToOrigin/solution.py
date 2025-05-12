from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        # Iterate through each point and calculate its squared distance to the origin
        for x, y in points:
            dist = (x ** 2) + (y ** 2)  # We use squared distance to avoid unnecessary square root computation
            min_heap.append([dist, x, y])  # Store distance along with point coordinates in the heap

        # Convert the list into a valid min-heap (heapify in-place)
        heapq.heapify(min_heap)

        output = []

        # Extract the k smallest elements (closest points to origin)
        while k > 0:
            dist, x, y = heapq.heappop(min_heap)  # Pop the point with the smallest distance
            output.append([x, y])  # Append only the coordinates (x, y) to the result
            k -= 1

        return output  # Return the k closest points