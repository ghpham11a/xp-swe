class FreqStack:

    def __init__(self):
        self.count = {}
        self.max_count = 0
        self.stacks = {}

    def push(self, val):
        val_count = 1 + self.count.get(val, 0)
        self.count[val] = val_count
        if val_count > self.max_count:
            self.max_count = val_count
            self.stacks[val_count] = []
        self.stacks[val_count].append(val)

    def pop(self):
        output = self.stacks[self.max_count].pop()
        self.count[output] -= 1
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        return output


test_operations = ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]
test_input = [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
test_output = []
test_freq_stack = None

for operation, operation_input in zip(test_operations, test_input):

    if operation == "FreqStack":
        test_freq_stack = FreqStack()
        test_output.append(None)

    if operation == "push":
        test_freq_stack.push(operation_input[0])
        test_output.append(None)

    if operation == "pop":
        test_output.append(test_freq_stack.pop())

assert(test_output == [None,None,None,None,None,None,None,5,7,5,4])

print("PASS")