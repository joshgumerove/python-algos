from linked_list_class import LinkedList


def partition(ll, x):
    current_node = ll.head
    ll.tail = ll.head

    while current_node:  # 11 # 2
        next_node = current_node.next  # 2 #100 # 30
        current_node.next = None

        if current_node.value < x:  # 2
            old_head = ll.head
            new_head = current_node
            new_head.next = old_head
            ll.head = new_head
        else:
            old_tail = ll.tail
            new_tail = current_node
            old_tail.next = new_tail
            ll.tail = new_tail

        current_node = next_node  # 100
    if ll.tail.next is not None:
        ll.tail.next = None
