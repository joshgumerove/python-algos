
class Node():
    def __init__(self, value = None): # default the value to None if no value is passed in
        self.value = value
        self.next = None

class CircularLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node # yielding the node value for iteration / this makes it easier to see the results in our output
            if node.next == self.head:
                break
            node = node.next
            
    def create_CSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node # to make the node reference itself / at creation will only be single node so head and tail should be the same
        self.head = node
        self.tail = node
        return "CSLL has been created"
            
    def insert_CSLL(self, nodeValue, location):
        if self.head is None:
            return "The head reference is None"
        else:
            new_node = Node(nodeValue)
            if location == 0:
                new_head = new_node
                current_head = self.head
                new_head.next = current_head
                self.head = new_head
                self.tail.next = self.head
            elif location == -1:
                new_tail = new_node
                current_tail = self.tail
                current_tail.next = new_tail
                new_tail.next = self.head
                self.tail = new_tail
                
            else:
                temp_location = 0
                current_node = self.head
                while temp_location < location -1:
                    current_node = current_node.next
                    temp_location += 1
                old_next = current_node.next
                new_next = new_node
                current_node.next = new_next
                new_next.next = old_next
                
    # note: traversal is exactly the same for this type of linked list
    def traversal(self):
        current_node = self.head
        if current_node is None:
            print("The List does not exist")
            return
        
        while current_node:
            print(f'current value: {current_node.value}')
            if current_node.next == self.head:
                break
            current_node = current_node.next
            
    def search_value(self, val):
        current_node = self.head 
        while current_node:
            if current_node.value == val:
                print('the value was found', current_node.value)
                return
            if current_node == self.tail:
                print('value not found')
                return
            
            current_node = current_node.next
            
    def SCLL_deletion(self, location):
        if location == 0:
            current_head = self.head
            new_head = current_head.next
            self.tail.next = new_head
            self.head = new_head
            return
            
        if location == -1:
            current_tail = self.tail
            current_node = self.head
            
            while current_node:
                if current_node.next == current_tail:
                    current_node.next = self.head
                    self.tail = current_node
                    return
                current_node = current_node.next
                
        current_location = 0
        current_node = self.head
        
        while current_location != location -1:
            current_node = current_node.next
            current_location += 1
            print(current_location, 'current location')
        nextNode = current_node.next
        print('what is next node: ', nextNode.value)
        current_node.next = nextNode.next
        print(current_node.next.value, 'this is new')
    
    def delete_entire_list(self):
        self.head = None
        self.tail.next = None
        self.tail = None
        
        
            
                
                
            
        
        
    
    
                    
                
        


# execution of DS
list_1 = CircularLinkedList()
list_1.create_CSLL(10)
list_1.insert_CSLL(50, 0) # insert at beginning
list_1.insert_CSLL(30, -1) # insert at end
list_1.insert_CSLL(1984, 1)
list_1.insert_CSLL(1985, 2)
list_1.insert_CSLL(50000, -1)
list_1.insert_CSLL(5000, -1)
list_1.insert_CSLL(520, -1)

print([node.value for node in list_1])
print(list_1.tail.value)
print(list_1.tail.next.value)
list_1.traversal()

# creating an empty list to test traversal
list_2 = CircularLinkedList()
list_2.traversal()

list_1.search_value(30)
list_1.search_value(300)
list_1.search_value(50)
print(list_1.tail.value)
print(list_1.head.value)
list_1.SCLL_deletion(1)
print(list_1.head.value, 'is')
print(list_1.tail.next.value, 'is')
print(list_1.tail.value, 'what is the value')
list_1.SCLL_deletion(-1)
print(list_1.tail.value, 'what is the value')

list_1.SCLL_deletion(5)

list_10 = CircularLinkedList()
list_10.create_CSLL(49)
list_10.insert_CSLL(50, 1)
list_10.insert_CSLL(51, 2)
list_10.insert_CSLL(52, 3)
list_10.insert_CSLL(53, 4)
print(list_10.head.value, "is")
print([node.value for node in list_10])
print(list_10.SCLL_deletion(2))
print([node.value for node in list_10])
list_10.delete_entire_list()
print([node.value for node in list_10])







