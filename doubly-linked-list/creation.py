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
        self.head = node
        self.tail = node
        
        return 'the DLL is created'
    
    def insertion(self, nodeValue, location):
        if location == 1:
            new_node = Node(nodeValue)
            old_head = self.head
            old_head.prev = new_node
            new_node.next = old_head
            self.head = new_node
            self.tail = old_head
            
        elif location == -1:
            new_node = Node(nodeValue)
            old_tail = self.tail
            old_tail.next = new_node
            new_node.prev = old_tail
            self.tail = new_node
            
        else:
            current_location = 1
            current_node = self.head
            while current_location != location -1:
                current_node = current_node.next
                current_location = current_location + 1
            new_node = Node(nodeValue)
            new_node.next = current_node.next
            new_node.prev = current_node
            new_node.next.prev = new_node
            current_node.next = new_node
                            
                
    
    
double_1 = DoubleLinkedList()
double_1.create_DLL(5)
double_1.insertion(4, 1)
double_1.insertion(6, -1)
double_1.insertion(50, -1)


print([node.value for node in double_1])
print(double_1.head.prev)
print(double_1.head.next.value)
print(double_1.tail.prev.value)


double_1.insertion(5000, 3)
double_1.insertion(100000, 1)
print([node.value for node in double_1])


                        
        