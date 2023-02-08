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

        

node_1 = Node()
list_1 = CircularLinkedList()

print(node_1.value)
