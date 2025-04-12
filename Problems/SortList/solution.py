
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def sort_list(self, head):
        
        # Base case: an empty list or a single-element list is already sorted.
        if head is None or head.next is None:
            return head
        
        # Use the fast and slow pointer technique to find the middle of the list.
        # 'slow' will move one step at a time while 'fast' moves two steps.
        # This allows 'slow' to reach the midpoint when 'fast' reaches the end.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 'slow' is now at the node just before the middle.
        # 'mid' starts at the next node, which is the beginning of the second half.
        mid = slow.next
        # Cut the list into two halves by setting the next pointer of the midpoint to None.
        slow.next = None

        # Recursively sort the first half.
        left_sorted = self.sort_list(head)
        # Recursively sort the second half.
        right_sorted = self.sort_list(mid)

        # Merge the two sorted halves and return the merged list.
        return self.merge(left_sorted, right_sorted)

    def merge(self, l1, l2):
        # Initialize a placeholder node to serve as the starting point of the merged list.
        # 'tail' will always point to the last node in the merged list.
        placeholder = tail = ListNode(0)
        
        # Continue merging as long as both lists have nodes remaining.
        while l1 and l2:
            # Compare current nodes of both lists.
            if l1.val <= l2.val:
                # Link the smaller node (l1) to the merged list.
                tail.next = l1
                l1 = l1.next  # Move l1 pointer forward.
            else:
                # Link the smaller node (l2) to the merged list.
                tail.next = l2
                l2 = l2.next  # Move l2 pointer forward.
            # Advance the tail pointer to the last node in the merged list.
            tail = tail.next

        # At this point, at least one of the lists is exhausted.
        # Attach the remaining elements (if any) from either list to the merged list.
        tail.next = l1 if l1 is not None else l2
        
        # Return the next node of placeholder because placeholder is a dummy starting node.
        return placeholder.next