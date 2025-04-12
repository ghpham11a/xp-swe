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
    
    def __repr__(self):
        # Generate a list of string representations for each value in the linked list.
        nodes = []
        current = self
        while current:
            nodes.append(str(current.val))
            current = current.next
        # Join the nodes with an arrow to indicate links.
        return " -> ".join(nodes) + " -> None"
    
def reverse_between(head, left, right):
    placeholder = ListNode(0, head)

    pre_left = placeholder
    while pre_left.next is not left:
        pre_left = pre_left.next 

    post_right = right.next

    prev = post_right
    current = left
    while current != post_right:
        nxt = current.next
        current.next = post_right
        prev = current
        current = nxt



def reverse_between(head, left, right):
    placeholder = ListNode(0, head)

    # Find the node that comes immediately before 'left'
    pre_left = placeholder
    while pre_left.next is not left:
        pre_left = pre_left.next

    # tail is the node that comes after 'right'
    post_right = right.next

    # Reverse the sublist from 'left' to 'right'
    prev = post_right  # This will be the next pointer for the new tail of reversed sublist.
    current = left
    while current != post_right:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    # Connect the previous part with the reversed sublist.
    pre_left.next = prev

    placeholder.next = None
    

test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
expected_list = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))

reverse_between(test_list, test_list.next, test_list.next.next.next)

assert(test_list == expected_list)

print("PASS")