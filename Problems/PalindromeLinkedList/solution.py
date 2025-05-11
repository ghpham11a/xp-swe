# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def is_palindrome(self, head):
        # Step 1: Use fast and slow pointers to find the middle of the linked list.
        # Fast moves 2 steps at a time, slow moves 1 step.
        # When fast reaches the end, slow will be at the midpoint.
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse the second half of the linked list starting from the middle.
        # This allows us to compare the first half and the reversed second half.
        prev = None
        while slow:
            tmp = slow.next       # Temporarily store the next node
            slow.next = prev      # Reverse the current node's pointer
            prev = slow           # Move prev to current node
            slow = tmp            # Move to next node in original order

        # Step 3: Compare the first half and the reversed second half.
        left, right = head, prev
        while right:  # Only need to compare till the end of second half
            if left.val != right.val:  # If any pair doesn't match, it's not a palindrome
                return False
            left = left.next
            right = right.next

        # If we successfully compared all corresponding nodes, it's a palindrome
        return True