class Stack():
    def __init__(self):
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

    def push(self, value):
        self.list.append(value)
        return 'The element has been successfully inserted'

    def pop(self):
        if self.is_empty():
            return 'the stack is empty'
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return 'the stack is empty'
        else:
            return self.list[-1]

    def delete(self):
        self.list = None


first_stack = Stack()
first_stack.push(10)
first_stack.push(15)

print(first_stack)
print(first_stack.is_empty())

first_stack.push(20)
print(first_stack)

first_stack.pop()
print(first_stack)
print(first_stack.peek())

first_stack.delete()

# should use Stack data structure when we utilize the latest data first
# example: back button in the browser
# peek(): returns the top element from the stack w/o removing it
# isEmpty(): checks if there are any elements in the stack
# isFull(): check if stack is full - note some languages have limits on list/array size
# delete(): delete entire stack
# implementing with a List is easy but may run into problems when stack grows
# implementing with a LinkedList has better performance
