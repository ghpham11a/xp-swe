from collections import deque

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def breadth_first_values(root):
    if root == None: return []

    values = []
    queue = deque()

    queue.appendleft(root) 

    while len(queue) > 0:

        curr_node = queue.pop()
        values.append(curr_node.value)

        if curr_node.left:
            queue.appendleft(curr_node.left)

        if curr_node.right:
            queue.appendleft(curr_node.right)

    return values

root = Node("a")
root.left = Node("b")
root.right = Node("c")
root.left.left = Node("d")
root.left.right = Node("e")
root.right.right = Node("f")

print(breadth_first_values(root))