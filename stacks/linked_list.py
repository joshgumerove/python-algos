class Node():
    def __init__(self, value):
        self.value = value
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Stack():
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(node.value) for node in self.linked_list]
        return '\n'.join(values)

    def is_empty(self):
        if self.linked_list.head is None:
            return True
        else:
            return False

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.linked_list.head  # note this line of code
        self.linked_list.head = new_node

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        else:
            old_head = self.linked_list.head.value
            self.linked_list.head = self.linked_list.head.next
            return old_head

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.linked_list.head.value

    def delete(self):
        self.linked_list.head = None


first_stack = Stack()
first_stack.push(10)
first_stack.push(20)
first_stack.push(30)

print(first_stack)
print("****************")

first_stack.pop()
print(first_stack)
print(first_stack.peek())

first_stack.delete()
print(first_stack)
