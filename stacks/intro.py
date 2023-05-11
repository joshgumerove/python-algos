class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        return self.stack


first_stack = Stack()
first_stack.push(10)
first_stack.push(15)
print(first_stack.push(20))
