class Heap():
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.heapSize = 0
        self.max_size = size + 1


def peek_of_heap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.custom_list[1]


new_heap = Heap(5)

print(new_heap.custom_list)
print(peek_of_heap(new_heap))
