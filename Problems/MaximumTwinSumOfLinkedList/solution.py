# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def pair_sum(self, head):
        
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        output = 0
        while slow:
            output = max(output, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return output