from linked_list_class import LinkedList


def nth_to_last(linkList, n):
    pointer1 = linkList.head
    pointer2 = linkList.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
# because pointer 2 is nth ahead
    while pointer2:
        print('************************')
        print('this is pointer1: ', pointer1)
        print('this is pointer2: ', pointer2)
        pointer1 = pointer1.next  # moving them at same pace
        pointer2 = pointer2.next
        print('************************')
        print('this is pointer1: ', pointer1)
        print('this is pointer2: ', pointer2)
    return pointer1


def nth_to_last2(linkedList, n):
    pointer1 = linkedList.head
    pointer2 = linkedList.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer2 = pointer2.next
        pointer1 = pointer1.next

    return pointer1


first_list = LinkedList()
first_list.generate(10, 0, 10000)
print(first_list)
print(nth_to_last(first_list, 2))
print(nth_to_last2(first_list, 2))
