from multiprocessing import Queue


custom_queue = Queue(maxsize=3)

custom_queue.put(5)
custom_queue.put(10)
custom_queue.put(15)

print(custom_queue.get())
print(custom_queue.qsize())
print(custom_queue.full())
print(custom_queue.empty())

custom_queue.put(30)

print(custom_queue.full())
print(custom_queue.empty())
