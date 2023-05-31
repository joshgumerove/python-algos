class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Queue():
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(node) for node in self.linked_list]
        return " ".join(values)

    def is_empty(self):
        if self.linked_list.head is None:
            return True
        else:
            return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = self.linked_list.tail.next

    def dequeue(self):
        if self.is_empty():
            return "no values to remove"

        temporary_val = self.linked_list.head

        if self.linked_list.head == self.linked_list.tail:
            self.linked_list.head = None
            self.linked_list.tail = None
            return temporary_val

        else:
            self.linked_list.head = self.linked_list.head.next
            return temporary_val

        self.linked_list.head = self.linked_list.head.next
        return temporary_val

    def peek(self):
        return self.linked_list.head.value

    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None


queue = Queue()
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)

print(queue.peek())
print(queue.is_empty())
print(queue)


queue.dequeue()
print(queue)
