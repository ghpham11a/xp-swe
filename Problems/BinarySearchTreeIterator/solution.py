# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        output_node = self.stack.pop()
        current = output_node.right
        while current:
            self.stack.append(current)
            current = current.left

        return output_node.val

    def has_next(self) :
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()