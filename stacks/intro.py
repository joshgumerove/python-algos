class Stack():
    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)


first_stack = Stack()
first_stack.push(10)
first_stack.push(15)
print(first_stack)

# should use Stack data structure when we utilize the latest data first
# example: back button in the browser
# peek(): returns the top element from the stack w/o removing it
# isEmpty(): checks if there are any elements in the stack
# isFull(): check if stack is full - note some languages have limits on list/array size
# delete(): delete entire stack
# implementing with a List is easy but may run into problems when stack grows
# implementing with a LinkedList has better performance
