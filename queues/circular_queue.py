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


first_queue = Queue(5)
print(first_queue)
print(first_queue.is_full())

# uses fixed capacity
# note how elements are ignored when enqueueing and dequeueing
# update top value and start value in queue
