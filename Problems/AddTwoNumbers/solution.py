class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(l1, l2):

    temp_head = ListNode()
    curr_head = temp_head
    carry = 0

    while l1 != None or l2 != None or carry != 0:
        l1_value = l1.val if l1 != None else 0
        l2_value = l2.val if l2 != None else 0
        curr_sum = l1_value + l2_value + carry
        carry = curr_sum // 10
        curr_head.next = ListNode(curr_sum % 10)
        curr_head = curr_head.next

        if l1 != None:
            l1 = l1.next
        if l2 != None:
            l2 = l2.next

    return temp_head.next