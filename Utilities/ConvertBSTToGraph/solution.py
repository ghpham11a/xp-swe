from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convert_to_graph(node):
    graph = {}

    recurse(graph, node, 0)

    return graph


def recurse(graph, node, parent):
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

    recurse(graph, node.left, node.val)
    recurse(graph, node.right, node.val)

# {1: [5, 3], 5: [1, 4], 4: [5, 9, 2], 9: [4], 2: [4], 3: [1, 10, 6], 10: [3], 6: [3]}