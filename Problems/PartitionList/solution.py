# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def partition(self, head: ListNode, x: int) -> ListNode:
        # Dummy heads for the two partitions:
        # - `left` will store nodes with values less than x
        # - `right` will store nodes with values greater than or equal to x
        left, right = ListNode(), ListNode()

        # Tail pointers to build the two separate lists
        left_tail, right_tail = left, right

        # Traverse the original list
        while head:
            if head.val < x:
                # Append current node to the `left` list
                left_tail.next = head
                left_tail = left_tail.next
            else:
                # Append current node to the `right` list
                right_tail.next = head
                right_tail = right_tail.next
            # Move to the next node
            head = head.next

        # Connect the end of the `left` list to the head of the `right` list
        left_tail.next = right.next

        # Important: terminate the `right` list to avoid cycles
        right_tail.next = None

        # Return the head of the new partitioned list (skip dummy head)
        return left.next