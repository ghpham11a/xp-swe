from collections import deque

class Solution:

    def can_reach(self, arr, start):

        queue = deque([start])

        while queue:
            node = queue.popleft()

            # check if reach zero
            if arr[node] == 0:
                return True

            if arr[node] < 0:
                continue

            # check available next steps
            for index in [node + arr[node], node - arr[node]]:
                if 0 <= index < len(arr):
                    queue.append(index)

            # mark as visited
            arr[node] = -arr[node]

        return False