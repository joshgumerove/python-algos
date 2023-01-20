# beginning of linked list study

# Singly Linked List: Creating

# Step 1: Create blank head and tail reference and initialize value with null

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
        

list1 = LinkedList()
print(list1)
print(list1.head)
print(list1.tail)

# Step 2: Create a blank Node

class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
node1 = Node(1)
node2 = Node(2)
print(node1)
print(node1.value)
print(node1.next)

# Step 3: link Head and Tail with Node

list1.head = node1
list1.head.next = node2
list1.tail = node2

print(list1.head.value)
print(list1.head.next)
print(list1.head.next.value)
print(list1.tail.value)