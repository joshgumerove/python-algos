class BinaryTree():
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_idx = 0
        self.max_size = size

    def insert_node(self, value):
        if self.last_used_idx + 1 is self.max_size:
            return "Binary Tree is full"
        self.custom_list[self.last_used_idx + 1] = value
        self.last_used_idx += 1
        return "Value successfully inserted"

    def search_node(self, nodeValue):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] is nodeValue:
                return "Success"
        return "Not found"

    def pre_order_traversal(self, index):
        if index > self.last_used_idx:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(index * 2)
        self.pre_order_traversal(index * 2 + 1)


b1 = BinaryTree(8)
b1.insert_node("Drinks")
b1.insert_node("Hot")
b1.insert_node('Cold')
b1.insert_node('Tea')
b1.insert_node('Coffee')

print(b1.custom_list)
print(b1.search_node("Hot"))
print(b1.search_node("Smoothie"))

print("*****pre_order_traversal*****")
b1.pre_order_traversal(1)
