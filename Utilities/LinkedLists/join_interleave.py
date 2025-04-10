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
    current1 = l1
    current2 = l2

    # Interweave nodes from l2 into l1.
    while current1 and current2:
        # Save pointers to the next nodes.
        next1 = current1.next
        next2 = current2.next

        # Insert current2 after current1.
        current1.next = current2
        current2.next = next1

        # Move to the next pair of nodes.
        current1 = next1
        current2 = next2

    # If l2 still has nodes left, attach them at the end of the merged list.
    if current2:
        # To attach the remaining nodes from l2, find the tail of l1.
        tail = l1
        while tail.next:
            tail = tail.next
        tail.next = current2
    
list_a = ListNode(1, ListNode(3, ListNode(5)))
list_b = ListNode(2, ListNode(4))

expected_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

interleave_linked_lists(list_a, list_b)

assert(list_a == expected_list)


print("PASS")