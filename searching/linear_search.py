def linear_search(my_list, target):
    for i in range(0, len(my_list)):
        if my_list[i] == target:
            return True
    return False


list1 = [2, 4, 6, 8]
print(linear_search(list1, 6))
print(linear_search(list1, 10))

# items are searched one-by-one in linear search
# good if list is not sorted
