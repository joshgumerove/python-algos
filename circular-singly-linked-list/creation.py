# similar to a regular singly linked list
# difference: last node in a circular linked list - points to the first node
# note: we can set the value of node.next to the node itself

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


# execution of DS
list_1 = CircularLinkedList()
list_1.create_CSLL(10)
print([node.value for node in list_1])

