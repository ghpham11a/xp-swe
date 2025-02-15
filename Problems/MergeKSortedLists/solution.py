
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    
    def merge_k_lists(self, lists):

        head = curr = ListNode(0)
           
        heap = []
        for i in range(len(lists)):
            if lists[i]: 
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            curr.next = node[2]  
            curr = curr.next
            
            if curr.next:
                heapq.heappush(heap, (curr.next.val, idx, curr.next))

        return head.next