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
            
    def insert(self, nodeValue, location):
        new_node = Node(nodeValue)
        if location == 1:
            new_node.prev = self.tail
            new_node.next = self.head
            new_node.next.prev = new_node
            self.head = new_node
            self.tail.next = new_node
                                
        elif location == -1:
            new_node.next = self.head
            new_node.prev = self.tail
            new_node.prev.next = new_node
            new_node.next.prev = new_node
            self.tail = new_node
                
        else:
            current_location = 1
            current_node = self.head
            while current_location < location - 1:
                current_node = current_node.next
                current_location += 1
            old_next = current_node.next
            current_node.next = new_node
            new_node.next = old_next
            old_next.prev = new_node
            current_node.next.prev = current_node
            
    def traverse(self): # should check if list has any values at beginning hypothetically
        current_node = self.head
        while current_node:
            print("the current value is: ", current_node.value)
            if current_node == self.tail:
                break
            current_node = current_node.next
            
    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print("reverse traversal value: ", current_node.value)
            if current_node == self.head:
                break
            current_node = current_node.prev
                               
double_1 = Circular_DLL()
double_1.create_CDLL(10)

print(double_1.head.prev.value)
print([node.value for node in double_1])

double_1.insert(100, 1)
double_1.insert(200, 1)
double_1.insert(5, -1)
double_1.insert(50000, 3)
double_1.insert(52525, -1)

print([node.value for node in double_1])
print(double_1.tail.next.value)

double_1.traverse()
double_1.reverse_traverse()
