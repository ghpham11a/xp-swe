"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        
        if not root:
            return root

        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        left_most = root

        while left_most.left:
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            current = left_most
            while current:

                # Connection 1
                current.left.next = current.right

                # Connection 2
                if current.next:
                    current.right.next = current.next.left

                # Progress along the list (nodes on the current level)
                current = current.next

            # Move onto the next level
            left_most = left_most.left

        return root