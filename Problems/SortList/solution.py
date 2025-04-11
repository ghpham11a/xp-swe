# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sort_list(self, head):
        
        if not head or not head.next:
            return head

        # split the list into two halfs
        left = head
        right = self.get_mid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sort_list(left)
        right = self.sort_list(right)
        return self.merge(left, right)

    def get_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        tail = placeholder = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return placeholder.next