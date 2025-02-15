class LRUNode:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = LRUNode(-1, -1)
        self.tail = LRUNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val
        
    def put(self, key, value):

        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        
        node = LRUNode(key, value)
        self.cache[key] = node
        self.add(node)
        
        if len(self.cache) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.cache[node_to_delete.key]

    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

test_input = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
test_output = []
test_commands = ["LRUCache","put","put","get","put","get","put","get","get","get"]

lru_cache = None

for index, command in enumerate(test_commands):

    if command == "LRUCache":
        lru_cache = LRUCache(test_input[index][0])
        test_output.append(None)

    if command == "put":
        lru_cache.put(test_input[index][0], test_input[index][1]) 
        test_output.append(None)

    if command == "get":
        value = lru_cache.get(test_input[index][0])
        test_output.append(value)

assert(test_output == [None,None,None,1,None,-1,None,-1,3,4])

print("PASS")


