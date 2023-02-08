# insertion into a Singly Linked List
# inserting a node into a singly linked list:
# most efficient is to add element at the beginning of Node (else will have to traverse)

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def insert_into_list(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                current_head = self.head
                new_head = new_node
                new_head.next = current_head
                self.head = new_head
            elif location == -1: # inserting at the end of the list (do not like the lecture functionality)
                current_tail = self.tail
                new_tail = new_node
                current_tail.next = new_tail
                self.tail = new_tail
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                old_next = temp_node.next
                new_next = new_node
                temp_node.next = new_next
                new_next.next = old_next
   
    # traversing a SSL
    def traverse_ssl(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head 
            while node is not None:
                print(node.value)
                node = node.next

    # searching for a value in linked list
    def search_value(self, value):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            postion = 0
            while node is not None:
                if node.value == value:
                    print(f"{value} found at postion {postion}")
                    return
                node = node.next
                postion += 1
                
        print("value not in list")
    
    # deleting from a singly linked list
    def delete_node(self, location):
        if self.head is None:
            print("the list does not exist")
        
        else:
            if location == 0:
                if self.head == self.tail: # note how we can check this
                    self.head = None
                    self.tail = None
                else:
                    current_head = self.head
                    next_head = current_head.next
                    self.head = next_head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    current_node = self.head
                    while current_node is not None:
                        if current_node.next == self.tail:
                            current_node.next = None
                            self.tail = current_node
                        else:
                            current_node = current_node.next
            else:
                current_node = self.head
                current_location = 0
                while current_location != location -1:
                    current_node = current_node.next
                    current_location += 1
                current_next = current_node.next
                new_next_node = current_next.next
                current_node.next = new_next_node
    
    def delete_list(self):
        self.head = None
        self.tail = None  
                
                            
                        

            
        
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
# list1 = LinkedList()

# list1.insert_into_list(5, 0)
# list1.insert_into_list(20, 0)
# list1.insert_into_list(99, 1)
# list1.insert_into_list(555, 1)

# print([node.value for node in list1])

# list2 = LinkedList()
# list2.insert_into_list(1, 1)
# list2.insert_into_list(2, 1)
# list2.insert_into_list(3, 1)
# list2.insert_into_list(4, 1)
# list2.insert_into_list(0, 0)
# list2.insert_into_list(0, 3) # inserted after the third element

# print([node.value for node in list2])
# list2.traverse_ssl()

# list1.search_value(99)

list3 = LinkedList()
list3.insert_into_list(10, 0)
list3.insert_into_list(5, -1)
list3.insert_into_list(19, 1)
list3.traverse_ssl()
list3.delete_node(0)

print("new linked list below")
list3.traverse_ssl()

print("testing tail functionality")
list3.insert_into_list(15, -1)
list3.insert_into_list(20, -1)
list3.insert_into_list(25, -1)
list3.traverse_ssl()

print("delete from end now")
list3.delete_node(-1)
list3.traverse_ssl()

print("remove from elsewhere")
list3.delete_node(2)
print([node.value for node in list3])
list3.delete_list()
print([node.value for node in list3])