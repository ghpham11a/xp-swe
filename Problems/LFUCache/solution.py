import collections

class LFUCache:

    def __init__(self, capacity):
        # Set the maximum capacity of the cache.
        self.cap = capacity
        # Dictionary mapping keys to their values.
        self.key2val = {}
        # Dictionary mapping keys to their current frequency of access.
        self.key2freq = {}
        # Dictionary mapping frequencies to an OrderedDict of keys.
        # The OrderedDict helps us identify the least recently used key for a given frequency.
        self.freq2key = collections.defaultdict(collections.OrderedDict)
        # Variable to keep track of the minimum frequency among all keys in the cache.
        self.minf = 0

    def get(self, key):
         # If the key is not found in the cache, return -1.
        if key not in self.key2val:
            return -1
        
        # Retrieve the current frequency of the key.
        oldfreq = self.key2freq[key]
        # Increment the frequency for this key as it is accessed.
        self.key2freq[key] = oldfreq + 1
        # Remove the key from its current frequency list.
        self.freq2key[oldfreq].pop(key)
        # If no keys remain with the old frequency, remove the frequency entry.
        if not self.freq2key[oldfreq]:
            del self.freq2key[oldfreq]

        # Add the key to the list for the new frequency.
        # The value '1' here is arbitrary; the OrderedDict is only used for ordering.
        self.freq2key[oldfreq + 1][key] = 1
        # If the current minimum frequency list is empty, update the min frequency.
        # This happens when the key we just updated was the only key at min frequency.
        if self.minf not in self.freq2key:
            self.minf += 1

        # Return the value associated with the key.
        return self.key2val[key]

    def put(self, key, value):
        # If the capacity is zero, no operation can be performed.
        if self.cap <= 0:
            return
        
        # If the key is already in the cache, update its value.
        # Note that we call get() to update the frequency.
        if key in self.key2val:
            self.get(key)
            self.key2val[key] = value
            return

        # If the cache is at full capacity, we need to remove the least frequently used key.
        if len(self.key2val) == self.cap:
            # Identify the least frequently used key.
            # Since freq2key[minf] is an OrderedDict, popitem(last=False) pops the least recently used key.
            delkey, _ = self.freq2key[self.minf].popitem(last=False)
            # Remove the key from key2val and key2freq dictionaries.
            del self.key2val[delkey]
            del self.key2freq[delkey]
        # Add the new key with its value to the cache.
        self.key2val[key] = value
        # Set its frequency to 1 (as it is newly added).
        self.key2freq[key] = 1
        # Insert the key into the frequency dictionary for frequency 1.
        self.freq2key[1][key] = 1
        # Reset the minimum frequency to 1 as a new key with frequency 1 is added.
        self.minf = 1

test_input = [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
test_output = []
test_commands = ["LFUCache","put","put","get","put","get","get","put","get","get","get"]

lru_cache = None

for index, command in enumerate(test_commands):

    if command == "LFUCache":
        lru_cache = LFUCache(test_input[index][0])
        test_output.append(None)

    if command == "put":
        lru_cache.put(test_input[index][0], test_input[index][1]) 
        test_output.append(None)

    if command == "get":
        value = lru_cache.get(test_input[index][0])
        test_output.append(value)

assert(test_output == [None,None,None,1,None,-1,3,None,-1,3,4])

print("PASS")