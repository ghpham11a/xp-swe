class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        current_self, current_other = self, other
        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return current_self is None and current_other is None

    def __str__(self):
        nodes = []
        current = self
        while current:
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes)


def merge_sort(head):
    # Base case: if the list is empty or has one node, it's already sorted.
    if head is None or head.next is None:
        return head

    # Split the list into two halves using the slow and fast pointer strategy.
    slow, fast = head, head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Disconnect the left half from the right half.
    prev.next = None

    # Recursively sort each half.
    left_sorted = merge_sort(head)
    right_sorted = merge_sort(slow)

    # Merge the two sorted halves.
    return merge(left_sorted, right_sorted)


def merge(l1, l2):
    dummy = tail = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 is not None else l2
    return dummy.next


test_list = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
expected_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

assert(merge_sort(test_list) == expected_list)

print("PASS")