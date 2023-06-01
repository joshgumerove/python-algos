from collections import deque

custom_queue = deque(maxlen=3)

custom_queue.append(2)
custom_queue.append(4)
custom_queue.append(6)

print(custom_queue)

custom_queue.popleft()

print(custom_queue)

custom_queue.clear()  # deletes all elements from queue

print(custom_queue)


# will override the first element if add another element because of maxSize
# note: deque objects are implemented as DLL which gives good performance
# part of python standard library
