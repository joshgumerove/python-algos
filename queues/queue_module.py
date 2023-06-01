from queue import Queue

custom_queue = Queue(maxsize=3)

print(custom_queue.qsize())
print(custom_queue.empty())

custom_queue.put(3)
custom_queue.put(6)
custom_queue.put(9)

print(custom_queue.qsize())
print(custom_queue.full())

print(custom_queue.get())  # performs same functionality as dequeue method
print(custom_queue.get())

print(custom_queue.qsize())

# note the three different types of queues: FIFO LIFO & Priority
# we implement only FIFO queue in this section
