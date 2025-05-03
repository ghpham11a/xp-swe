from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Handle the edge case: if the input node is None, return None
        if not node:
            return node

        # Initialize the BFS queue
        q = deque()
        q.appendleft(node)

        # Dictionary to map original nodes to their cloned copies
        source_to_clone = {}
        
        # Clone the first node and store it in the map
        source_to_clone[node] = Node(node.val, [])

        # Start BFS traversal
        while q:
            # Get the next node from the queue
            current_node = q.pop()

            # Iterate through the current node's neighbors
            for neighbor in current_node.neighbors:
                # If this neighbor hasn't been cloned yet
                if neighbor not in source_to_clone:
                    # Clone it and add to the map
                    source_to_clone[neighbor] = Node(neighbor.val, [])
                    # Enqueue it for further processing
                    q.appendleft(neighbor)

                # Append the cloned neighbor to the current node's clone neighbor list
                source_to_clone[current_node].neighbors.append(source_to_clone[neighbor])

        # Return the clone of the original input node
        return source_to_clone[node]