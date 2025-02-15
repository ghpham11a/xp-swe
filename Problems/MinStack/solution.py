class MinStack:

    def __init__(self):
        self.val_stack = []
        self.min_stack = []

    def push(self, val) :
        self.val_stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self):
        self.val_stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.val_stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()