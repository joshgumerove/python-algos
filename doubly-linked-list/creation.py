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
            
        elif location == -1:
            new_node = Node(nodeValue)
            old_tail = self.tail
            old_tail.next = new_node
            new_node.prev = old_tail
            self.tail = new_node
            
        else:
            current_location = 1
            current_node = self.head
            while current_location < location:
                current_node = current_node.next
                current_location = current_location + 1
            new_node = Node(nodeValue)
            new_node.next = current_node.next
            new_node.prev = current_node
            new_node.next.prev = new_node
            current_node.next = new_node
            
    def traverse(self):
        if self.head is None:
            print("there is no linked list")
        else: 
            current_node = self.head
            while current_node:
                print("the value is: ", current_node.value)
                current_node = current_node.next
        return 'done'
    
    def reverse_traverse(self):
        if self.head is None:
            print("there is no value")
        else:
            current_node = self.tail
            while current_node:
                print(current_node.value, "look")
                current_node = current_node.prev
            return "done"
        
    def search_value(self, value):
        if self.head is None:
            return "no linked list"
        
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return f"your value has been found: {current_node.value}"
            current_node = current_node.next
        return 'value not found'
    
    def delete_node(self, location):
        if location == 1:
            current_node = self.head
            if self.head.next is None:
                current_node = None
            else:
                old_head = current_node
                new_head = old_head.next
                new_head.prev = None
                self.head = new_head
        elif location == -1:
            current_node = self.tail
            if self.tail.prev is None:
                self.tail = None
                self.head = None
            else:
                old_tail = current_node
                new_tail = old_tail.prev
                self.tail = new_tail  
        else:
            current_location = 1
            current_node = self.head
            while current_location < location -1:
                current_node = current_node.next
                current_location +=1
            old_previous = current_node.prev
            old_next = current_node.next
            current_node.prev = old_previous.prev
            current_node.next = old_next.next
            
                
        
                            
                
    
    
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

double_1.traverse()
double_1.reverse_traverse()
double_2 = DoubleLinkedList()
double_2.traverse()

print(double_2.tail)
print(double_1.search_value(50))

print([node.value for node in double_1])
double_1.delete_node(1)
print([node.value for node in double_1])
double_1.delete_node(-1)
print([node.value for node in double_1])
double_1.delete_node(3)
print([node.value for node in double_1])

# double_3 = DoubleLinkedList()
# double_3.create_DLL(10)
# print([node.value for node in double_3])

# print([node.value for node in double_3])
# double_3.delete_node(-1)
# print([node.value for node in double_3])
# print(double_3.head)






                        
        