from heapq import heappush, heappop
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        m = len(nums1)  # Length of the first array
        n = len(nums2)  # Length of the second array

        ans = []        # Final answer list to store the k pairs
        visited = set() # Set to track (i, j) index pairs we have already pushed into the heap

        # Min-heap to store tuples of (sum of pair, (index in nums1, index in nums2))
        # Start with the first pair (0,0) - the sum of the smallest elements from both arrays
        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))

        while k > 0 and minHeap:
            # Pop the smallest sum pair from the heap
            val, (i, j) = heappop(minHeap)
            # Append the actual pair values to the answer list
            ans.append([nums1[i], nums2[j]])

            # If there's a next element in nums1, push the new pair (i+1, j) into the heap
            if i + 1 < m and (i + 1, j) not in visited:
                heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))  # Mark this index pair as visited

            # If there's a next element in nums2, push the new pair (i, j+1) into the heap
            if j + 1 < n and (i, j + 1) not in visited:
                heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))  # Mark this index pair as visited

            # Decrement k after adding one pair to the answer
            k -= 1
        
        return ans