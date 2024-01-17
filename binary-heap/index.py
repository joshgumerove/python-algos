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


def heapify_tree_extract(rootNode, index, heapType):
    left_index = index * 2
    right_index = index * 2 + 1
    swap_child = 0

    if rootNode.heap_size < left_index:
        return
    elif rootNode.heap_size == left_index:
        if heapType == "Min":
            if rootNode.custom_list[index] > rootNode.custom_list[left_index]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[left_index]
                rootNode.custom_list[left_index] = temp
            return
        else:
            if rootNode.custom_list[index] < rootNode.custom_list[left_index]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[left_index]
                rootNode.custom_list[left_index] = temp
            return
    else:
        if heapType == "Min":
            if rootNode.custom_list[left_index] < rootNode.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if rootNode.custom_list[index] > rootNode.custom_list[swap_child]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[swap_child]
                rootNode.custom_list[swap_child] = temp
        else:
            if rootNode.custom_list[left_index] > rootNode.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if rootNode.custom_list[index] < rootNode.custom_list[swap_child]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[swap_child]
                rootNode.custom_list[swap_child] = temp
        heapify_tree_extract(rootNode, swap_child, heapType)


def extract_node(rootNode, heapType):
    if rootNode.heap_size == 0:
        return
    else:
        extracted_node = rootNode.custom_list[1]
        rootNode.custom_list[1] = rootNode.custom_list[rootNode.heap_size]
        rootNode.custom_list[rootNode.heap_size] = None
        rootNode.heap_size -= 1
        heapify_tree_extract(rootNode, 1, heapType)
        return extracted_node


new_heap = Heap(5)
insert_node(new_heap, 4, "Max")
insert_node(new_heap, 5, "Max")
insert_node(new_heap, 2, "Max")
insert_node(new_heap, 1, "Max")
print(extract_node(new_heap, "Max"))
print("**level order traverse**")
level_order_traversal(new_heap)

# print(new_heap.custom_list)
# print(peek_of_heap(new_heap))
# print(size_of_heap(new_heap))

# print("**traversal**")
# level_order_traversal(new_heap)

# insert_node(new_heap, 5, "Min")
# insert_node(new_heap, 1, "Min")

# print("**traversal**")
# level_order_traversal(new_heap)
