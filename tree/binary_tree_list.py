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

    def in_order_traversal(self, index):
        if index > self.last_used_idx:
            return
        self.in_order_traversal(index * 2)
        print(self.custom_list[index])
        self.in_order_traversal(index * 2 + 1)

    def post_order_traversal(self, index):
        if index > self.last_used_idx:
            return
        self.post_order_traversal(index * 2)
        self.post_order_traversal(index * 2 + 1)
        print(self.custom_list[index])

    def level_order_traversal(self, index):
        for i in range(index, self.last_used_idx + 1):
            print(self.custom_list[i])


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
print("*****in_order_traversal*****")
b1.in_order_traversal(1)
print("********post_order_traversal*******")
b1.post_order_traversal(1)
print('******level_order_traversal*******')
b1.level_order_traversal(1)
