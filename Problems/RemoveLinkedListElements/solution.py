# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def remove_elements(self, head, val):
        # Create a dummy node that points to the head.
        # This simplifies removal of nodes at the head of the list.
        dummy = ListNode(-1, head)
        
        # Initialize 'prev' as the dummy node and 'curr' as the head of the list.
        prev = dummy
        curr = head
        
        # Traverse the linked list until 'curr' becomes None.
        while curr:
            # If the current node's value matches the target value,
            # adjust the previous node's next pointer to skip the current node.
            if curr.val == val:
                prev.next = curr.next  # Remove the current node.
            else:
                # Otherwise, move the 'prev' pointer to the current node.
                prev = curr
            
            # Move 'curr' to the next node in the list.
            curr = curr.next
        
        # Return the new head of the list, which is the node after the dummy node.
        return dummy.next