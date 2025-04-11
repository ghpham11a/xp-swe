
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

    def reverse_k_group(self, head, k):
        placeholder = ListNode(-1, head)
        
        group_prev = placeholder

        while True:
            kth = self.get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            prev = kth.next
            curr = group_prev.next
            while curr != group_next:
                next_node = curr.next
                curr.next = prev

                prev = curr
                curr = next_node

            tmp = group_prev.next 
            group_prev.next = kth
            group_prev = tmp

        return placeholder.next

    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
expected_list = ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5)))))

solution = Solution()

assert(solution.reverse_k_group(test_list, 2) == expected_list)
    
print("PASS")