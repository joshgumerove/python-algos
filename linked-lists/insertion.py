# insertion into a Singly Linked List
# inserting a node into a singly linked list:
# most efficient is to add element at the beginning of Node (else will have to traverse)

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
        
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
list1 = LinkedList()
node1 = Node(5)

print(list1, node1)