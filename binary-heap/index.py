class Heap():
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1


def peek_of_heap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.custom_list[1]


def size_of_heap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heap_size


def level_order_traversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heap_size + 1):
            print(rootNode.custom_list[i])


new_heap = Heap(5)

print(new_heap.custom_list)
print(peek_of_heap(new_heap))
print(size_of_heap(new_heap))

print("**traversal**")
print(level_order_traversal(new_heap))
