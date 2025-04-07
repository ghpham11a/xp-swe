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
    
def find_middle(head):

    slow = fast = head 
    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next

    return slow


list_a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
list_b = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

assert(find_middle(list_a) == ListNode(3))
assert(find_middle(list_b) == ListNode(4))

print("PASS")

