class BSTNode():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_node(rootNode, value):
    if rootNode.data is None:
        rootNode.data = value
    elif value <= rootNode.data:
        if rootNode.left_child is None:
            rootNode.left_child = BSTNode(value)
        else:
            insert_node(rootNode.left_child, value)
    else:
        if rootNode.right_child is None:
            rootNode.right_child = BSTNode(value)
        else:
            insert_node(rootNode.right_child, value)
    return "The node has been successfully inserted"


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


def min_value_node(bstNode):
    current = bstNode
    while current.left_child is not None:
        current = current.left_child
    return current


def delete_node(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.left_child = delete_node(rootNode.left_child, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right_child = delete_node(rootNode.right_child, nodeValue)
    else:
        if rootNode.left_child is None:
            temp = rootNode.right_child
            rootNode = None
            return temp
        if rootNode.right_child is None:
            temp = rootNode.left_child
            rootNode = None
            return temp
        temp = min_value_node(rootNode.right_child)
        rootNode.data = temp.data
        rootNode.right_child = delete_node(rootNode.right_child, temp.data)
    return rootNode


new_BST = BSTNode(None)

insert_node(new_BST, 70)
insert_node(new_BST, 50)
insert_node(new_BST, 90)
insert_node(new_BST, 30)
insert_node(new_BST, 60)
insert_node(new_BST, 80)
insert_node(new_BST, 100)
insert_node(new_BST, 20)
insert_node(new_BST, 40)

print(new_BST.data)
print(new_BST.left_child.data)

print('***pre-order-traversal***')
pre_order_traversal(new_BST)

print('***in-order-traversal***')
in_order_traversal(new_BST)

print('***post-order-traversal***')
post_order_traversal(new_BST)

search_node(new_BST, 60)

print("***DELETE_NODE")
delete_node(new_BST, 80)
delete_node(new_BST, 90)
in_order_traversal(new_BST)
