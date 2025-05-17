
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    
    def flatten(self, head):
        # Stack will store next nodes that we need to visit later
        stack = []

        # Start from the head of the list
        curr = head

        # First pass: process all nodes and flatten children in-place
        while curr:

            # If current node has a child
            if curr.child:
                # If there's a next node, push it onto the stack to revisit later
                if curr.next:
                    stack.append(curr.next)
                    # Detach the next node from current to prevent back-reference issues
                    curr.next.prev = None

                # Point current's next to the child
                curr.next = curr.child
                # Set child's prev pointer to current
                curr.child.prev = curr
                # Remove the child pointer (we're flattening it)
                curr.child = None

            # Move to the next node if it exists
            if curr.next:
                curr = curr.next
            else:
                break  # End of this level reached

        # Second pass: connect any deferred nodes from the stack
        while stack:
            # Pop a previously saved `next` node and attach it
            curr.next = stack.pop()
            curr.next.prev = curr

            # Traverse through this attached segment until the end
            while curr.next:
                curr = curr.next

        # Return the head of the flattened list
        return head
