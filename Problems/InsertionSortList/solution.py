# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class Solution:

    def insertion_sort_list(self, head):
        # Create a dummy node (placeholder) that acts as the new starting point of the sorted list.
        # This simplifies edge cases such as inserting at the head of the list.
        placeholder = ListNode(0, head)
        
        # Initialize two pointers:
        # 'prev' points to the last node of the sorted portion of the list.
        # 'curr' is the node that will be evaluated for insertion into the sorted sublist.
        prev, curr = head, head.next

        # Iterate through the list until there are no more unsorted nodes.
        while curr:
            # If the current node's value is greater than or equal to the previous node's value,
            # then it's already in the correct position and we can move forward.
            if curr.val >= prev.val:
                # Move both pointers one step forward.
                prev, curr = curr, curr.next
                continue  # Continue to the next iteration of the loop.

            # Otherwise, find the correct position to insert 'curr' in the sorted portion.
            # Start from the dummy node.
            tmp = placeholder
            # Traverse the sorted part until you find the node after which the current node should be inserted.
            while curr.val > tmp.next.val:
                tmp = tmp.next

            # Rearrange pointers to remove 'curr' from its current position.
            # 'prev.next' skips over 'curr', effectively removing it from its original spot.
            prev.next = curr.next

            # Insert 'curr' between 'tmp' and 'tmp.next'.
            # First, point 'curr.next' to the node that comes after 'tmp'.
            curr.next = tmp.next
            # Then, point 'tmp.next' to 'curr', completing the insertion.
            tmp.next = curr

            # Update 'curr' to continue iterating from the next node in the unsorted portion.
            # Since 'prev' still points to the last element in the sorted portion, 
            # 'prev.next' is the next unsorted node.
            curr = prev.next

        # Return the new head of the sorted list.
        # Since 'placeholder' is a dummy node, the actual sorted list starts at 'placeholder.next'.
        return placeholder.next