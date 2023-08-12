class BinaryTree():
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_idx = 0
        self.max_size = size


b1 = BinaryTree(8)
