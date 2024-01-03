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


def heapify_tree_insert(rootNode, index, heapType):
    parent_index = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.custom_list[index] < rootNode.custom_list[parent_index]:
            temp = rootNode.custom_list[index]
            rootNode.custom_list[index] = rootNode.custom_list[parent_index]
            rootNode.custom_list[parent_index] = temp
        heapify_tree_insert(rootNode, parent_index, heapType)
    elif heapType == "Max":
        if rootNode.custom_list[index] > rootNode.custom_list[parent_index]:
            temp = rootNode.custom_list[index]
            rootNode.custom_list[index] = rootNode.custom_list[parent_index]
            rootNode.custom_list[parent_index] = temp
        heapify_tree_insert(rootNode, parent_index, heapType)


def insert_node(rootNode, nodeValue, heapType):
    if rootNode.heap_size + 1 == rootNode.max_size:
        return "Binary Heap is full"
    rootNode.custom_list[rootNode.heap_size + 1] = nodeValue
    rootNode.heap_size += 1
    heapify_tree_insert(rootNode, rootNode.heap_size, heapType)
    return "value successfully inserted"


new_heap = Heap(5)

print(new_heap.custom_list)
print(peek_of_heap(new_heap))
print(size_of_heap(new_heap))

print("**traversal**")
level_order_traversal(new_heap)

insert_node(new_heap, 5, "Min")
insert_node(new_heap, 1, "Min")

print("**traversal**")
level_order_traversal(new_heap)
