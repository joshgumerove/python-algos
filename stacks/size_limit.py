class Stack():
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        list_copy = self.list[:]
        values = list_copy.reverse()
        values = [str(x) for x in list_copy]
        return '\n'.join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def is_full(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            return 'stack is already at capacity'
        else:
            self.list.append(value)
            return 'element successfully inserted'

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return 'list is empty'
        else:
            return self.list[-1]

    def delete(self):
        self.list = None
        self.maxSize = None


custom_stack = Stack(4)
print(custom_stack.is_empty())
print(custom_stack.is_full())
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
print(custom_stack)
print(custom_stack.peek())
custom_stack.delete()
