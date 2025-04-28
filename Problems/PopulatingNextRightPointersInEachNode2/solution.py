
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        
        # Start with the root node
        current = root
        
        # Dummy node that helps in connecting nodes at the next level
        dummy = Node(0)

        while current:
            # Initialize tail for the next level
            tail = dummy
            dummy.next = None  # Reset dummy for the next level

            # Traverse nodes at the current level
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                current = current.next  # Move to next node in current level using already established next pointers

            # After the current level is processed, move to the next level
            current = dummy.next

        return root