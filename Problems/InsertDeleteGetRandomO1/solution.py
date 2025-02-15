class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False

        self.num_map[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_map:
            return False

        index = self.num_map[val]
        last_val = self.nums[-1]
        self.nums[index] = last_val
        self.nums.pop()
        self.num_map[last_val] = index
        del self.num_map[val]

        return True

    def getRandom(self) -> int:
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

    if operation == "remove"
        test_output.append(randomized_set.remove(test_input[index][0])) 

    if operation == "getRandom":
        test_output.append(randomized_set.getRandom())

assert(test_output == [None,True,False,True,2,True,False,2])

print("PASS")