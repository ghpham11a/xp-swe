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
    
def interleave_linked_lists(l1, l2):
    # Create a dummy node to simplify list construction.
    dummy = ListNode()
    # 'curr' will be used to build the new interleaved list.
    curr = dummy

    # Process both lists while both have nodes.
    while l1 and l2:
        # Append a node from l1.
        curr.next = l1
        l1 = l1.next
        curr = curr.next

        # Append a node from l2.
        curr.next = l2
        l2 = l2.next
        curr = curr.next

    # If one list is longer, attach the remaining nodes.
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2

    # Return the head of the new list, skipping the dummy node.
    return dummy.next


list_a = ListNode(1, ListNode(3, ListNode(5)))
list_b = ListNode(2, ListNode(4))

expected_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

assert(interleave_linked_lists(list_a, list_b) == expected_list)


print("PASS")