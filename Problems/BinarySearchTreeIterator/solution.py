# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:

    def __init__(self, root):
        # Stack is used to simulate the recursion stack for in-order traversal
        self.stack = []

        # Initialize the stack with the leftmost path from the root
        # because the smallest element in a BST is the leftmost node
        while root:
            self.stack.append(root)
            root = root.left

        # (Optional) Print the initial stack size for debugging
        print(len(self.stack))

    def next(self) -> int:
        # Pop the top node from the stack (current smallest unvisited node)
        output_node = self.stack.pop()

        # If the popped node has a right child, process its leftmost path
        # because the next smallest node will be in the right subtree
        current = output_node.right
        while current:
            self.stack.append(current)
            current = current.left

        # Return the value of the node as part of in-order traversal
        return output_node.val

    def hasNext(self) -> bool:
        # Return True if there are still nodes left to process
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()