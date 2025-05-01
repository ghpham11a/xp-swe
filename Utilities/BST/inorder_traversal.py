class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def iterative_inorder_traversal(root):

    stack = []
    current = root
    output = []

    while stack or current:
        # Go as far left as possible
        while current:
            stack.append(current)
            current = current.left

        # Process the node
        current =  stack.pop()
        output.append(current.val)

        # Move to the right subtree
        current = current.right

    return output

def recursive_inorder_traversal(root):
    output = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        output.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return output
