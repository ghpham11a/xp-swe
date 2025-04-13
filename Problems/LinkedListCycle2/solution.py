class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def detect_cycle(self, head):
        
        # Initialize both slow and fast pointers to the head of the list.
        slow = head
        fast = head
        
        # Flag to indicate whether a meeting point was found
        met = False

        # Traverse the list with slow pointer moving one step and fast pointer moving two steps.
        while fast is not None and fast.next is not None:
            # Move slow pointer by one node
            slow = slow.next
            # Move fast pointer by two nodes          
            fast = fast.next.next   

            # If the slow and fast pointers meet, it means there is a cycle in the list.
            if slow == fast:
                # A cycle has been detected.
                met = True
                # Exit the loop as meeting point is found.
                break

        # If the pointers never met, there is no cycle in the list.
        if not met:
            return None
        
        # To find the start of the cycle, reset the slow pointer to the head.
        slow = head 
        
        # Move both pointers one step at a time until they meet.
        # The meeting point will be at the start of the cycle.
        while slow != fast:
            slow = slow.next        # Move one step from the head.
            fast = fast.next        # Continue moving from the meeting point.

        # Both pointers now meet at the start of the cycle.
        return slow

solution = Solution()

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

assert(solution.detect_cycle(node1) == node2)

print("PASS")