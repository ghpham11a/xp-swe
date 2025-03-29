class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def detect_cycle(self, head):
        
        slow = head
        fast = head
        met = False

        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast:
                met = True
                break 

        if met == False:
            return None
        
        slow = head 
        while slow != fast:
            slow = slow.next 
            fast = fast.next 

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