from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def amount_of_time(self, root, start):
        graph = {}  # Dictionary to represent the tree as an undirected graph

        # Step 1: Convert the binary tree into an undirected graph
        self.convert_to_graph(graph, root, 0)

        queue = deque([start])  # Queue for BFS, starting with the infected node
        minute = 0              # Tracks how many minutes have passed
        visited = {start}       # Set to track visited/infected nodes

        # Step 2: Perform BFS from the start node to simulate infection spread
        while queue:
            level_size = len(queue)  # Number of nodes infected this minute

            while level_size > 0:
                current = queue.popleft()
                
                # Infect adjacent (connected) nodes
                for num in graph[current]:
                    if num not in visited:
                        visited.add(num)
                        queue.append(num)
                
                level_size -= 1

            minute += 1  # One minute passes after processing current level

        return minute - 1  # Subtract 1 because the last increment happens after all nodes are infected

    def convert_to_graph(self, graph, node, parent):
        # Base case: reached a leaf's child
        if node is None:
            return

        # Initialize list of adjacent nodes for this node
        if node.val not in graph:
            graph[node.val] = []

        # Connect current node with its parent to make the graph undirected
        if parent != 0:
            graph[node.val].append(parent)

        # Connect current node to left and right children if they exist
        if node.left:
            graph[node.val].append(node.left.val)
        if node.right:
            graph[node.val].append(node.right.val)

        # Recursively convert left and right subtrees
        self.convert_to_graph(graph, node.left, node.val)
        self.convert_to_graph(graph, node.right, node.val)