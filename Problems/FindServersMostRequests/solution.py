from typing import List 

import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Count of requests handled by each server
        count = [0] * k
        
        # 'busy' is a min-heap storing (end_time, server_id) for each busy server
        # 'free' is a sorted list or heap of free server indices (transformed below)
        busy, free = [], list(range(k))

        for i, start in enumerate(arrival):
            # Free up any servers whose tasks have completed before the current start time
            while busy and busy[0][0] <= start:
                _, server_id = heapq.heappop(busy)
                # Push server back to free list using a wrapped index to preserve order
                heapq.heappush(free, i + (server_id - i) % k)

            if free:
                # Choose the next available server based on the problem's logic:
                # - Start with i % k
                # - Try next available from there (wrapping around)
                # By pushing i + offset into free, and popping, we simulate a rotating priority queue
                busy_id = heapq.heappop(free) % k

                # Mark server as busy until start + load[i]
                heapq.heappush(busy, (start + load[i], busy_id))

                # Increment the count of requests handled by this server
                count[busy_id] += 1
        
        # Identify the maximum number of requests handled
        max_job = max(count)

        # Return list of all server IDs with this maximum request count
        return [i for i, n in enumerate(count) if n == max_job]