# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def delete_middle(self, head):

        # If the list contains only one node, remove it and return None
        if head.next is None:
            return None

        # Initialize two pointers:
        # - 'slow' will move one step at a time
        # - 'fast' will move two steps at a time
        # 'prev' keeps track of the node before 'slow'
        slow = head
        fast = head
        prev = None

        # Traverse the list to find the middle node
        # When 'fast' reaches the end, 'slow' will be at the middle
        while fast and fast.next:
            prev = slow           # Save the node before the middle
            slow = slow.next      # Move slow by 1 step
            fast = fast.next.next # Move fast by 2 steps

        # Remove the middle node by linking the previous node to the node after 'slow'
        prev.next = slow.next

        # Return the modified head of the list
        return head