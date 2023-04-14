class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def create_DLL(self, nodeValue):
        node = Node(nodeValue)
        # node.prev = None
        # node.next = None
        self.head = node
        self.tail = node
        
        return 'the DLL is created'
    
    
double_1 = DoubleLinkedList()
double_1.create_DLL(5)
print(double_1.head.prev)
print([node.value for node in double_1])
                        
        