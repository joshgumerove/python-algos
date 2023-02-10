
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
        
        
    
    
                    
                
        


# execution of DS
list_1 = CircularLinkedList()
list_1.create_CSLL(10)
list_1.insert_CSLL(50, 0) # insert at beginning
list_1.insert_CSLL(30, -1) # insert at end
list_1.insert_CSLL(1984, 1)
list_1.insert_CSLL(1985, 2)
print([node.value for node in list_1])
print(list_1.tail.value)
print(list_1.tail.next.value)
list_1.traversal()

# creating an empty list to test traversal
list_2 = CircularLinkedList()
list_2.traversal()






