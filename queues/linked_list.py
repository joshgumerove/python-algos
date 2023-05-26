class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def dequeue(self):
        if self.is_empty():
            return "no values to remove"
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    def peek(self):
        return self.head.value

    def delete(self):
        self.head = None
        self.tail = None


queue = LinkedList()
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)

print(queue.head.value)
print(queue.tail.value)

print(queue.dequeue())
print(queue.head.value)
print(queue.peek())
print(queue.is_empty())

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
