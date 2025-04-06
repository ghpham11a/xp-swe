
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorder_list(self, head):
        # Use two pointers (slow and fast) to find the middle of the linked list.
        # 'slow' moves one step at a time, 'fast' moves two steps.
        # When 'fast' reaches the end, 'slow' will be at the middle.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # At this point, 'slow' is at the middle of the list.
        # The next step is to reverse the second half of the list.
        # 'second' will be the head of the second half.
        second = slow.next
        # Disconnect the first half from the second half.
        slow.next = None
        prev = None

        # Reverse the second half of the list.
        while second:
            # Temporarily store the next node.
            tmp = second.next
            # Reverse the pointer of the current node.
            second.next = prev
            # Move 'prev' to the current node.
            prev = second
            # Move to the next node in the original second half.
            second = tmp

        # After the loop, 'prev' is the head of the reversed second half.
        # Now, merge the two halves of the list.

        # Pointer to the beginning of the first half.
        first = head
        # Pointer to the beginning of the reversed second half.      
        second = prev

        # Merge the two halves by alternating nodes from each half.
        while second:
            # Store the next nodes temporarily.
            tmp1 = first.next
            tmp2 = second.next

            # Link the current node of the first half to the current node of the second half.
            first.next = second
            # Link the current node of the second half to the next node of the first half.
            second.next = tmp1

            # Move both pointers forward.
            first = tmp1
            second = tmp2


        