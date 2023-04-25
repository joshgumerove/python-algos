class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
        
class Circular_DLL():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def create_CDLL(self, nodeValue):
        new_node = Node(nodeValue)
        self.head = new_node
        self.tail = new_node
        new_node.prev = new_node
        new_node.next = new_node
        print("created cirlce DLL")
                
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

        
double_1 = Circular_DLL()
double_1.create_CDLL(10)
print(double_1.head.prev.value)
print([node.value for node in double_1])