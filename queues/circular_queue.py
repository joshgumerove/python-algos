class Queue():
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def is_full(self):
        if (self.top + 1) == self.start:
            return True
        elif (self.start == 0) and (self.top + 1 == self.maxSize):
            return True
        else:
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.is_full():
            return "the queue is already full"
        else:
            if (self.top + 1) == self.maxSize:  # points to the last element therefore update to zero
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
                self.items[self.top] = value
                return "the element is inserted at the end of the queue"

    def dequeue(self):
        if self.is_empty():
            return "there is no element in the queue"

        first_element = self.items[self.start]
        start = self.start

        if self.start == self.top:
            self.start = -1
            self.top = -1
        elif (self.start + 1) == self.maxSize:
            self.start = 0
        else:
            self.start += 1
        self.items[start] = None
        return first_element

    def peek(self):
        if self.is_empty():
            return "there is no element in the queue"
        return self.items[self.start]


custom_queue = Queue(5)
print(custom_queue)
print(custom_queue.is_full())
print(custom_queue.is_empty())

custom_queue.enqueue(10)
custom_queue.enqueue(9)
custom_queue.enqueue(8)
custom_queue.enqueue(7)
custom_queue.enqueue(6)

print(custom_queue)
print(custom_queue.top, "is the top")
print(custom_queue.start, "is the start")
print(custom_queue.is_full())
print(custom_queue.is_empty())

print(custom_queue.dequeue())
print(custom_queue)
print("***")
print(custom_queue.is_full())
print(custom_queue.enqueue(900))
print(custom_queue)
print(custom_queue.peek())

# uses fixed capacity
# note how elements are ignored when enqueueing and dequeueing
# update top value and start value in queue
