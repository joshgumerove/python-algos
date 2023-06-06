# implement queue using two stacks

class Stack():
    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self) == 0:
            return None
        return self.list.pop()


class QueueViaStack():
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def __str__(self):
        return str([self.in_stack.list, self.out_stack.list])

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        while len(self.in_stack):
            temp_val = self.in_stack.pop()
            self.out_stack.push(temp_val)
        removed_val = self.out_stack.pop()

        while len(self.out_stack):
            temp_val = self.out_stack.pop()
            self.in_stack.push(temp_val)
        return removed_val


custom_queue = QueueViaStack()
custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)
custom_queue.enqueue(4)

print(custom_queue)
print(custom_queue.dequeue())
print(custom_queue)
