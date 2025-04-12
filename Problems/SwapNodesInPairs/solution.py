# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0, nxt=None):
        self.val = x
        self.next = nxt

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

    def swap_pairs(self, head):

        # Create a dummy node. This is used to simplify edge cases, such as when the head node is swapped.
        dummy = ListNode(-1)
        dummy.next = head  # The dummy node's next pointer now points to the head of the original list.

        # The prev_node always points to the node preceding the pair that will be swapped.
        # Initially, it is set to the dummy node.
        prev_node = dummy

        # Loop through the list until we reach the end or there is no pair left to swap.
        while head and head.next:
            # Identify the two nodes that will be swapped:
            first_node = head          # The first node of the pair.
            second_node = head.next    # The second node of the pair.

            # Begin swapping the identified nodes.
            # 1. Connect the previous part of the list with the second node.
            prev_node.next = second_node
            # 2. Link the first node to the node following the second node.
            first_node.next = second_node.next
            # 3. Complete the swap by linking the second node to the first node.
            second_node.next = first_node

            # Reinitialize prev_node and head for the next pair swap.
            # After the swap, the first_node has moved one position forward and becomes the previous node for the next pair.
            prev_node = first_node
            # Move head to the next pair to be swapped.
            head = first_node.next

        # Return the head of the new, modified list.
        # The dummy node's next pointer points to the new head after all swaps.
        return dummy.next
    
test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
expected_list = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))

solution = Solution()

assert(solution.swap_pairs(test_list) == expected_list)

print("PASS")