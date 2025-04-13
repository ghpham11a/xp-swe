# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, value):
        # Check if 'other' is an instance of ListNode
        if not isinstance(value, ListNode):
            return False

        # Initialize two pointers for each list.
        current_self, current_other = self, value
        
        # Traverse both lists concurrently.
        while current_self is not None and current_other is not None:
            # If values differ at any node, the lists are not equal.
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
        
        # If both lists have reached their end, they are equal.
        # If one list still has nodes left, they are not equal.
        return current_self is None and current_other is None

class Solution:

    def reverse_between(self, head, left, right):
        placeholder = ListNode(0, head)

        left_prev, curr = placeholder, head
        for _ in range(left - 1):
            left_prev, curr = curr, curr.next

        prev = None
        for _ in range(right - left + 1):
            tmp_next = curr.next
            curr.next = prev
            prev, curr = curr, tmp_next

        left_prev.next.next = curr
        left_prev.next = prev

        return placeholder.next
    

test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
expected_list = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))

solution = Solution()

solution.reverse_between(test_list, 2, 4)

assert(test_list == expected_list)

print("PASS")
    
