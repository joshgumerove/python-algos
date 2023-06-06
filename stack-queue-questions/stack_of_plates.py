class PlateStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return str(self.stacks)

    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])  # add new stack with item

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()  # remove from the last stack

    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None


custom_stack = PlateStack(2)
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)

print(custom_stack)
print(custom_stack.pop())
print(custom_stack.pop())
print(custom_stack)

custom_stack.push(5)
custom_stack.push(6)
custom_stack.push(7)
custom_stack.push(8)

print(custom_stack)
print(custom_stack.pop_at(2))
print(custom_stack)
