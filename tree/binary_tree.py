class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


new_bt = TreeNode('Drinks')
left_child = TreeNode("Hot")
right_child = TreeNode("Cold")

new_bt.left_child = left_child
new_bt.right_child = right_child

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")

left_child.left_child = tea
left_child.right_child = coffee


def pre_order_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


pre_order_traversal(new_bt)


def in_order_traversal(root_node):
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


print("*****************************************")
in_order_traversal(new_bt)


def post_order_traversal(root_node):
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


print("*****************************************")
post_order_traversal(new_bt)

# each node has at most two children
# different kinds of binary trees
# note the different ways to traverse a binary tree


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Queue():
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(node) for node in self.linked_list]
        return " ".join(values)

    def is_empty(self):
        if self.linked_list.head is None:
            return True
        else:
            return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = self.linked_list.tail.next

    def dequeue(self):
        if self.is_empty():
            return "no values to remove"

        temporary_val = self.linked_list.head

        if self.linked_list.head == self.linked_list.tail:
            self.linked_list.head = None
            self.linked_list.tail = None
            return temporary_val

        else:
            self.linked_list.head = self.linked_list.head.next
            return temporary_val

    def peek(self):
        if self.linked_list.head is not None:
            return self.linked_list.head.value
        else:
            return "no elements in the queue"

    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None


def level_order_traversal(root_node):  # go level by level
    if not root_node:
        return
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        print(root.value.data)
        if root.value.left_child is not None:
            custom_queue.enqueue(root.value.left_child)
        if root.value.right_child is not None:
            custom_queue.enqueue(root.value.right_child)


level_order_traversal(new_bt)


def search_bt(root_node, node_value):
    if not root_node:
        return "The Binary Tree does not exist"
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.value.data == node_value:
                return True
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
    return "Not Found"


print(search_bt(new_bt, "This should return not found"))
print(search_bt(new_bt, "Tea"))


def insert_node(root_node, new_node):
    if not root_node:
        root_node = new_node
        return root_node

    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        if root.value.left_child is not None:
            custom_queue.enqueue(root.value.left_child)
        else:
            root.value.left_child = new_node
            return "successfully inserted left child"
        if root.value.right_child is not None:
            custom_queue.enqueue(root.value.right_child)
        else:
            root.value.right_child = new_node
            return "successfully inserted right child"


new_node = TreeNode("Cola")
print(insert_node(new_bt, new_node))
level_order_traversal(new_bt)


def get_deepest_node(root_node):
    if not root_node:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
        deepest_node = root.value
        return deepest_node


print("***********************")
deepest_node = get_deepest_node(new_bt)
print(deepest_node.data)


def delete_deepest_node(root_node, deepest_node):
    if not root_node:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.value is deepest_node:
                root.value = None
                return
            if root.value.right_child:
                if root.value.right_child is deepest_node:
                    root.value.right_child = None
                    return
                else:
                    custom_queue.enqueue(root.value.right_child)
            if root.value.left_child:
                if root.value.left_child is deepest_node:
                    root.value.left_child = None
                    return
                else:
                    custom_queue.enqueue(root.value.left_child)


# print("[get_deepest_node]")
# new_node = get_deepest_node(new_bt)
# print("[delete_deepest_node]")
# delete_deepest_node(new_bt, new_node)
# print("[level_order_traversal]")
# level_order_traversal(new_bt)

def delete_node_BT(root_node, node):
    if not root_node:
        return "the binary tree does not exist"
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.value.data == node:
                temp_node = get_deepest_node(root_node)
                root.value.data = temp_node.data
                delete_deepest_node(root_node, temp_node)
                return "The node has been successfully deleted"
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
        return "Failed to delete node"


print("[delete_node_BT]")
delete_node_BT(new_bt, "Hot")
level_order_traversal(new_bt)


def delete_BT(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The binary tree has been deleted"


print("[delete_BT]")
delete_BT(new_bt)
level_order_traversal(new_bt)
