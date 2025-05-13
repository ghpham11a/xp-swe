from typing import Optional

class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node which will act as the starting point of our resulting linked list.
        temp_head = ListNode()
        # Set a pointer to traverse and build the new list, starting from the dummy node.
        curr_head = temp_head
        # Initialize a variable to store any carry-over value when the sum of two digits is 10 or greater.
        carry = 0

        # Continue looping until all nodes in l1 and l2 have been processed and no carry remains.
        while l1 is not None or l2 is not None or carry != 0:
            # Get the current value from l1 if it exists; otherwise, use 0.
            l1_value = l1.val if l1 is not None else 0
            # Get the current value from l2 if it exists; otherwise, use 0.
            l2_value = l2.val if l2 is not None else 0
            
            # Calculate the sum of the two values plus any carry from the previous iteration.
            curr_sum = l1_value + l2_value + carry
            # Update the carry for the next iteration by dividing the current sum by 10.
            carry = curr_sum // 10
            # The new node's value is the remainder when the current sum is divided by 10.
            curr_head.next = ListNode(curr_sum % 10)

            # Move the pointer to the next node in the result list.
            curr_head = curr_head.next
            # Advance to the next node in l1 if it exists.
            if l1 is not None:
                l1 = l1.next
            # Advance to the next node in l2 if it exists.
            if l2 is not None:
                l2 = l2.next

        # Return the next node of the dummy node which is the actual head of the resultant list.
        return temp_head.next