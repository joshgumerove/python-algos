from linked_list_class import LinkedList
from math import floor


def sum_list(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0  # will also be a temporary variable
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = int(result / 10)

    if carry > 0:
        ll.add(1)  # did not consider this in lecture
    return ll


first_list = LinkedList()
first_list.generate(3, 0, 10)
second_list = LinkedList()
second_list.generate(3, 0, 9)
print(first_list)
print(second_list)

print(sum_list(first_list, second_list))
