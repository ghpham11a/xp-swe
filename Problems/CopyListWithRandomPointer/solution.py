class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:

    def copy_random_list(self, head):

        # Dictionary to map original nodes to their corresponding new (copied) nodes.
        # We initialize it with None mapped to None to simplify pointer assignment later.
        old_to_copy = {None: None}

        # First pass: Create a copy of each node in the original list (ignoring next and random pointers).
        curr_node = head
        while curr_node:
            # Create a new node with the same value as the current node.
            copy_node = Node(curr_node.val)
            # Store the mapping from the original node to its copy.
            old_to_copy[curr_node] = copy_node
            # Move to the next node in the original list.
            curr_node = curr_node.next

        # Second pass: Assign the next and random pointers for each copied node.
        curr_node = head
        while curr_node:
            # Retrieve the copied node corresponding to the current original node.
            copy_node = old_to_copy[curr_node]
            # Set the 'next' pointer by using the mapping from the original node's next node.
            # If curr_node.next is None, old_to_copy[None] returns None.
            copy_node.next = old_to_copy[curr_node.next]
            # Set the 'random' pointer similarly using the mapping for the original node's random pointer.
            copy_node.random = old_to_copy[curr_node.random]
            # Move to the next original node.
            curr_node = curr_node.next

        # Return the head of the copied list (which is the copy of the original head).
        return old_to_copy[head]