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


new_AVL = AVLNode(10)
print(new_AVL.data)
