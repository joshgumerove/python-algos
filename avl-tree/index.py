class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1  # need height property to determine if AVL is balanced


new_AVL = AVLNode()
print(new_AVL)
