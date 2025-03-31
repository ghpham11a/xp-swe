class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def floyd(head):

    tortoise = head
    hare = head
    while hare is not None and hare.next is not None:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            break
  
    # Find the position μ of first repetition.
    index_of_start_of_cycle = 0
    tortoise = head
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next
        index_of_start_of_cycle += 1
 
    # Find the length of the shortest cycle starting from x_μ.
    length_of_cycle = 1
    hare = tortoise.next
    while tortoise != hare:
        hare = hare.next
        length_of_cycle += 1
 
    return (length_of_cycle, index_of_start_of_cycle)

def create_list_with_cycle(values, cycle_entry):

    nodes = [ListNode(x) for x in values]

    # Link the nodes in sequence.
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    # Create a cycle: last node points to the first node.
    nodes[-1].next = nodes[cycle_entry]

    return nodes[0]

assert(floyd(create_list_with_cycle([3,2,0,-4], 1)) == (3, 1))
assert(floyd(create_list_with_cycle([1,3,4,2,2], 3)) == (2, 3))

print("PASS")