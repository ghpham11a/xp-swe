import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val    # The value of the node.
        self.next = next  # Pointer to the next node in the list.

class Solution(object):
    
    def merge_k_lists(self, lists):
        # Create a dummy node which will serve as the start of the merged list.
        # 'head' will remain the dummy reference; 'curr' will be used to build the merged list.
        head = curr = ListNode(0)
        
        # Initialize an empty min-heap.
        # We'll use the heap to always extract the node with the smallest value.
        heap = []
        
        # Iterate over each linked list in the input array.
        for i in range(len(lists)):
            # If the current list is not empty, push a tuple into the heap.
            # The tuple consists of:
            #   (node value, list index, node reference)
            # The list index is used to break ties when two nodes have the same value.
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                
        # Continue the process until the heap is empty.
        while heap:
            # Pop the smallest element from the heap.
            # 'node' is a tuple: (node value, list index, node reference)
            node = heapq.heappop(heap)
            idx = node[1]  # The index of the linked list from which this node comes.
            
            # Attach the extracted node to the merged list.
            curr.next = node[2]
            curr = curr.next  # Move the current pointer to the new node.
            
            # If there is a next node in the list from which the node was extracted,
            # push it into the heap so that it can be merged later.
            if curr.next:
                heapq.heappush(heap, (curr.next.val, idx, curr.next))

        # Return the merged list, starting after the dummy node.
        return head.next
