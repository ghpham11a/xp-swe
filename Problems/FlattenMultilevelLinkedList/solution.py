"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head):

        stack = []

        curr = head

        while curr:

            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                    curr.next.prev = None

                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None

            if curr.next:
                curr = curr.next
            else:
                break

        while stack:
            curr.next = stack.pop()
            curr.next.prev = curr

            while curr.next:
                curr = curr.next

        return head
