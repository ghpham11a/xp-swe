"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copy_random_list(self, head):

        old_to_copy = {None: None}

        curr_node = head
        while curr_node:
            copy_node = Node(curr_node.val)
            old_to_copy[curr_node] = copy_node
            curr_node = curr_node.next

        curr_node = head
        while curr_node:
            copy_node = old_to_copy[curr_node]

            copy_node.next = old_to_copy[curr_node.next] 
            copy_node.random = old_to_copy[curr_node.random]

            curr_node = curr_node.next

        return old_to_copy[head]