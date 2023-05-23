class Queue():
    def __init__(self, maxSize):
        self.items = maxSize * [None]

# uses fixed capacity
# note how elements are ignored when enqueueing and dequeueing
# update top value and start value in queue
