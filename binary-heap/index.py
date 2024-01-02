class Heap():
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.heapSize = 0
        self.max_size = size + 1


new_heap = Heap(2)
print(new_heap.custom_list)
