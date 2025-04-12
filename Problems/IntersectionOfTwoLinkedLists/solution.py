# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_intersection_node(self, headA, headB):
        
         # Initialize two pointers starting at the heads of each list.
        l1, l2 = headA, headB
        
        # Continue looping until the two pointers meet.
        while l1 != l2:
            # Advance l1 to the next node, or switch to headB if l1 is None.
            l1 = l1.next if l1 else headB
            # Advance l2 to the next node, or switch to headA if l2 is None.
            l2 = l2.next if l2 else headA
            
        # When l1 equals l2, it could be at the intersection node, or both are None (no intersection).
        return l1