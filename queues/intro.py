class Queue():
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(item) for item in self.items]

        return " ".join(values)

    def enqueue(self, value):
        self.items.append(value)

    def is_empty(self):
        if len(self.items):
            return False
        return True

    def dequeue(self):
        if self.is_empty():
            return "no values in queue"
        self.items.remove(self.items[0])

    def peek(self):
        if self.is_empty():
            return "no values in queue"
        return self.items[0]

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
print(custom_queue)
custom_queue.dequeue()
print(custom_queue)
custom_queue.dequeue()
print(custom_queue.peek())
print(custom_queue.dequeue())
print(custom_queue.dequeue())
print(custom_queue.dequeue())
print(custom_queue.dequeue())
custom_queue.enqueue(10)
print(custom_queue)
custom_queue.delete()
print(custom_queue.peek())
