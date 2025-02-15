from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def amount_of_time(self, root, start):
        graph = {}

        self.convert_to_graph(graph, root, 0)

        queue = deque([start])
        minute = 0
        visited = {start}

        while queue:
            level_size = len(queue)
            while level_size > 0:
                current = queue.popleft()
                for num in graph[current]:
                    if num not in visited:
                        visited.add(num)
                        queue.append(num)
                level_size -= 1
            minute += 1

        return minute - 1

    def convert_to_graph(self, graph, node, parent):
        if node is None:
            return

        if node.val not in graph:
            graph[node.val] = []

        if parent != 0:
            graph[node.val].append(parent)

        if node.left:
            graph[node.val].append(node.left.val)

        if node.right:
            graph[node.val].append(node.right.val)

        self.convert_to_graph(graph, node.left, node.val)
        self.convert_to_graph(graph, node.right, node.val)