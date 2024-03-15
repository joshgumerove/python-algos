def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return -1


list1 = [2, 4, 6, 8]
print(linear_search(list1, 6))
print(linear_search(list1, 10))

# items are searched one-by-one in linear search
# good if list is not sorted
