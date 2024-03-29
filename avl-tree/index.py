from queues import Queue


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1  # need height property to determine if AVL is balanced


def pre_order_traversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    pre_order_traversal(rootNode.left_child)
    pre_order_traversal(rootNode.right_child)


def in_order_traversal(rootNode):
    if not rootNode:
        return
    in_order_traversal(rootNode.left_child)
    print(rootNode.data)
    in_order_traversal(rootNode.right_child)


def post_order_traversal(rootNode):
    if not rootNode:
        return
    post_order_traversal(rootNode.left_child)
    post_order_traversal(rootNode.right_child)
    print(rootNode.data)


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


def search_node(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print(f"the value is found: {nodeValue}")
    elif nodeValue < rootNode.data:
        if rootNode.left_child.data == nodeValue:
            print(f"the value is found: {nodeValue}")
        else:
            search_node(rootNode.left_child, nodeValue)

    else:
        if rootNode.right_child.data == nodeValue:
            print(f"the value is found: {nodeValue}")
        else:
            search_node(rootNode.right_child, nodeValue)


def get_height(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def right_rotate(disbalancedNode):
    new_root = disbalancedNode.left_child
    disbalancedNode.left_child = disbalancedNode.left_child.right_child
    new_root.right_child = disbalancedNode
    disbalancedNode.height = 1 + max(get_height(disbalancedNode.left_child),
                                     get_height(disbalancedNode.right_child))
    new_root.height = max(get_height(new_root.left_child),
                          get_height(new_root.right_child))
    return new_root


def left_rotate(disbalancedNode):
    new_root = disbalancedNode.right_child
    disbalancedNode.right_child = disbalancedNode.right_child.left_child
    new_root.left_child = disbalancedNode
    disbalancedNode.height = 1 + max(get_height(disbalancedNode.left_child),
                                     get_height(disbalancedNode.right_child))
    new_root.height = max(get_height(new_root.left_child),
                          get_height(new_root.right_child))
    return new_root


def get_balance(rootNode):
    if not rootNode:
        return 0
    return get_height(rootNode.left_child) - get_height(rootNode.right_child)


def insert_node(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.left_child = insert_node(rootNode.left_child, nodeValue)
    else:
        rootNode.right_child = insert_node(rootNode.right_child, nodeValue)

    rootNode.height = 1 + max(get_height(rootNode.left_child),
                              get_height(rootNode.right_child))
    balance = get_balance(rootNode)
    if balance > 1 and nodeValue < rootNode.left_child.data:
        return right_rotate(rootNode)
    if balance > 1 and nodeValue > rootNode.left_child.data:
        rootNode.left_child = left_rotate(rootNode.left_child)
        return right_rotate(rootNode)
    if balance < -1 and nodeValue > rootNode.right_child.data:
        return left_rotate(rootNode)
    if balance < -1 and nodeValue < rootNode.right_child.data:
        rootNode.right_child = right_rotate(rootNode.right_child)
        left_rotate(rootNode)
    return rootNode


def get_min_value_node(rootNode):
    if rootNode is None or rootNode.left_child is None:
        return rootNode
    return get_min_value_node(rootNode.left_child)


def delete_node(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.left_child = delete_node(rootNode.left_child, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right_child = delete_node(rootNode.right_child, nodeValue)
    else:
        if rootNode.left_child is None:
            temp = rootNode.right_child
            rootNode = None
            return temp
        elif rootNode.right_child is None:
            temp = rootNode.left_child
            rootNode = None
            return temp
        temp = get_min_value_node(rootNode.right_child)
        rootNode.data = temp.data
        rootNode.right_child = delete_node(rootNode.right_child, temp.data)
    balance = get_balance(rootNode)
    if balance > 1 and get_balance(rootNode.left_child) >= 0:
        return right_rotate(rootNode)
    if balance < -1 and get_balance(rootNode.right_child) <= 0:
        return left_rotate(rootNode)
    if balance > 1 and get_balance(rootNode.left_child) < 0:
        rootNode.left_child = left_rotate(rootNode.left_child)
        return right_rotate(rootNode)
    if balance < -1 and get_balance(rootNode.right_child):
        rootNode.right_child = right_rotate(rootNode.right_child)
        return left_rotate(rootNode)
    return rootNode


def delete_AVL(rootNode):
    rootNode.data = None
    rootNode.left_child = None
    rootNode.right_child = None
    return "AVL deleted"


new_AVL = AVLNode(5)
new_AVL = insert_node(new_AVL, 10)
new_AVL = insert_node(new_AVL, 15)
new_AVL = insert_node(new_AVL, 20)
new_AVL = delete_node(new_AVL, 15)
level_order_traversal(new_AVL)
delete_AVL(new_AVL)

level_order_traversal(new_AVL)
