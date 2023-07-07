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
