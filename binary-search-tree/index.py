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


new_BST = BSTNode(None)

insert_node(new_BST, 10)
insert_node(new_BST, 7)
print(new_BST.data)
print(new_BST.left_child.data)
