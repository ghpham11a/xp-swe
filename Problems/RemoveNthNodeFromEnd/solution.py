# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):

        # Create a dummy (placeholder) node that points to the head.
        # This simplifies edge cases such as removing the first node.
        placeholder = ListNode(0, head)
        
        # Initialize two pointers: 'left' will eventually point to the node
        # immediately before the target node for removal.
        left = placeholder
        
        # 'right' is set to the start of the list (head) to establish a gap.
        right = head
        
        # Move 'right' pointer n steps ahead to maintain a gap of n nodes.
        # This means when 'right' reaches the end, 'left' will be right before the node to remove.
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers until 'right' reaches the end of the list.
        # At each step, 'left' is advanced by one node maintaining the gap.
        while right:
            left = left.next
            right = right.next

        # 'left.next' is the node that needs to be removed.
        # Skip this node by linking 'left' to 'left.next.next'.
        left.next = left.next.next

        # Return the head of the modified list (which is placeholder.next,
        # as placeholder might be pointing to a new head in case the original head is removed).
        return placeholder.next