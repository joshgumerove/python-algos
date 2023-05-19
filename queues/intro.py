class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.insert(0, value)

    def is_empty(self):
        if len(self.items):
            return False
        return True

    def dequeue(self):
        if self.is_empty():
            return "no values in queue"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "no values in queue"
        return self.items[-1]

    def delete(self):
        self.items = []


# first in first out structure
# like an actually line in real life
# elements must be removed from the beginning of he queue
# remove method: referred to as dequeue
# insert method: referred to as enqueue

custom_queue = Queue()
custom_queue.enqueue(5)
custom_queue.enqueue(10)
custom_queue.enqueue(15)
custom_queue.enqueue(20)
print(custom_queue.dequeue())
print(custom_queue.dequeue())
print(custom_queue.peek())
print(custom_queue.dequeue())
print(custom_queue.dequeue())
print(custom_queue.dequeue())
print(custom_queue.dequeue())
custom_queue.delete()
print(custom_queue.peek())
