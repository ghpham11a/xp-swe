import random

class RandomizedSet:

    def __init__(self):
        # Dictionary to map a value to its index in the list
        self.num_map = {}
        # List to store the actual elements
        self.nums = []

    def insert(self, val: int) -> bool:
        # If val already exists, do not insert it
        if val in self.num_map:
            return False

        # Otherwise, add val to the end of the list
        self.nums.append(val)
        # And record its index in the map
        self.num_map[val] = len(self.nums) - 1

        return True

    def remove(self, val: int) -> bool:
        # If val doesn't exist, can't remove it
        if val not in self.num_map:
            return False

        # Get the index of the element to remove
        index = self.num_map[val]
        # Get the last element in the list
        last_val = self.nums[-1]

        # Move the last element into the spot of the element to remove
        self.nums[index] = last_val
        # Update the moved element's index in the map
        self.num_map[last_val] = index

        # Remove the last element (now a duplicate) from the list
        self.nums.pop()
        # Remove the element from the map
        del self.num_map[val]

        return True

    def getRandom(self) -> int:
        # Randomly return an element from the list
        return random.choice(self.nums)



test_operations = ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
test_input = [[],[1],[2],[2],[],[1],[2],[]]
test_output = []

randomized_set = None

for index, operation in enumerate(test_operations):

    if operation == "RandomizedSet":
        randomized_set = RandomizedSet()
        test_output.append(None)

    if operation == "insert":
        test_output.append(randomized_set.insert(test_input[index][0])) 

    if operation == "remove":
        test_output.append(randomized_set.remove(test_input[index][0])) 

    if operation == "getRandom":
        test_output.append(randomized_set.getRandom())

assert(test_output == [None,True,False,True,2,True,False,2])

print("PASS")