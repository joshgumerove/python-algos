class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
        
class Circular_DLL():
    def __init__(self):
        self.head = None
        self.tail = None