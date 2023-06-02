# QUESTION: describe how you could use a single Python list to implement three stacks
# NOTES: fixed division approach

class MultiStack():
    def __init__(self, stackSize):
        self.number_stacks = 3
        self.custom_list = [0] * (stackSize * self.number_stacks)
        self.sizes = [0] * self.number_stacks
        self.stack_size = stackSize
        # creates list with specified number of elements

    def is_full(self, stackNumber):
        if self.sizes[stackNumber] == self.stack_size:
            return True
        else:
            return False

    def is_empty(self, stackNumber):
        if self.sizes[stackNumber] == 0:
            return True
        else:
            return False

    def index_of_top(self, stackNum):  # helper method
        offset = stackNum * self.stack_size
        return offset + self.sizes[stackNum] - 1

    def push(self, item, stackNum):
        if self.is_full(stackNum):
            return 'The stack is full'
        else:
            self.sizes[stackNum] += 1
            self.custom_list[self.index_of_top(stackNum)] = item

    def pop(self, stackNum):
        if self.is_empty(stackNum):
            return "The stack is empty"
        else:
            temporary_top = self.custom_list[self.index_of_top(stackNum)]
            self.custom_list[self.index_of_top(stackNum)] = 0
            self.sizes[stackNum] -= 1
            return temporary_top
