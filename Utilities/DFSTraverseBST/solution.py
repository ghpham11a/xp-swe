class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def depth_first_values(root):
    if root == None: return []

    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)

    return [root.value] + left_values + right_values

root = Node("a")
root.left = Node("b")
root.right = Node("c")
root.left.left = Node("d")
root.left.right = Node("e")
root.right.right = Node("f")

print(depth_first_values(root))