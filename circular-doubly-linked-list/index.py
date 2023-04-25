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
            if self.head == self.tail:
                old_head = self.head
                new_head = new_node
                new_head.next = old_head
                new_head.next.prev = new_head
                old_head.next = new_head
                self.head = new_head
                self.tail = old_head
                
            else:
                old_head = self.head
                new_head = new_node
                new_head.next = old_head
                new_head.next.prev = new_head
                new_head.prev = self.tail
                new_head.prev.next = new_head
                self.head = new_head
                
        elif location == -1:
            if self.head == self.tail:
                old_tail = self.tail
                new_tail = new_node
                old_tail.next = new_tail
                old_tail.next.prev = old_tail
                self.tail = new_tail
            else:
                old_tail = self.tail
                new_tail = new_node
                old_tail.next = new_tail
                old_tail.next.prev = old_tail
                new_tail.next = self.head
                new_tail.next.prev = new_tail
                self.tail = new_tail
                
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
