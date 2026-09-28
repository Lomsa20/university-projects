class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    def pop(self):
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
    def top(self): return self.stack[-1]
    def getMin(self): return self.min_stack[-1]
k = MinStack()
k.push(1)
k.push(-5)
k.push(3)
k.push(-4)
print(k.getMin())
print(k.top())
