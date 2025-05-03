from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # If the list is empty, there's nothing to rotate
        if not head:
            return head

        # First, find the length of the list and the tail node
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        # Use modulo to avoid unnecessary full rotations
        k = k % length

        # If k is 0 after modulo, list remains unchanged
        if k == 0:
            return head

        # Move to the (length - k - 1)th node; this will be the new tail
        curr = head
        for i in range(length - k - 1):
            curr = curr.next

        # The node after `curr` becomes the new head
        new_head = curr.next

        # Break the link to form new tail
        curr.next = None

        # Connect the old tail to the original head
        tail.next = head

        # Return the new head of the rotated list
        return new_head