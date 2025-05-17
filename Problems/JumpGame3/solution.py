from collections import deque

class Solution:

    def can_reach(self, arr, start):
        # Use a queue for BFS traversal, starting from the `start` index
        queue = deque([start])

        while queue:
            # Get the current index from the front of the queue
            node = queue.popleft()

            # If we've reached a value of 0, return True
            if arr[node] == 0:
                return True

            # If this node has already been visited (marked negative), skip it
            if arr[node] < 0:
                continue

            # Calculate the next possible jumps: forward and backward
            for index in [node + arr[node], node - arr[node]]:
                # Only proceed if the new index is within bounds
                if 0 <= index < len(arr):
                    queue.append(index)

            # Mark this node as visited by negating its value
            arr[node] = -arr[node]

        # If we finish BFS without reaching a zero, return False
        return False