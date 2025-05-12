from typing import List
import collections

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # If the source and target are the same, no buses are needed
        if source == target:
            return 0

        # Map each stop to all buses (by index) that go through it
        graph = collections.defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)

        # Queue for BFS traversal, starting from the source stop with 0 buses taken
        queue = collections.deque([(source, 0)])

        visited_stops = set()   # Keep track of stops we've already visited
        visited_buses = set()   # Keep track of buses we've already taken

        while queue:
            stop, route_len = queue.popleft()

            # If we reached the target stop, return the number of buses taken
            if stop == target:
                return route_len

            # Explore all buses available from this stop
            for bus in graph[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)  # Mark this bus as used

                    # Add all the stops reachable from this bus to the queue
                    for next_stop in routes[bus]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, route_len + 1))  # +1 since we took a new bus

        # If we exhaust the queue without reaching the target, return -1
        return -1