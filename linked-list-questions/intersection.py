from linked_list_class import LinkedList, Node


def intersection(LLA, LLB):
    if LLA.tail is not LLB.tail:
        return

    # if make it past the conditon above already no they intersect

    len_a = len(LLA)
    len_b = len(LLB)

    shorter = LLA if len_a < len_b else LLB
    longer = LLB if len_a < len_b else LLA

    diff = len(longer) - len(shorter)

    longer_node = longer.head
    shorter_node = shorter.head

    for i in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


def add_same_node(LLA, LLB, value):
    temp_node = Node(value)
    LLA.tail.next = temp_node
    LLB.tail.next = temp_node
    LLA.tail = temp_node
    LLB.tail = temp_node

# note: intersection is based on reference and not value


list_a = LinkedList()
list_a.generate(5, 0, 15)

list_b = LinkedList()
list_b.generate(8, 0, 15)

add_same_node(list_a, list_b, 90)

print(list_a)
print(list_b)
print(intersection(list_a, list_b))
