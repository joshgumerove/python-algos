# Is Unique: implment an algorithm to determine if a list has all unique characters using python list


my_list = [1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]

def is_unique(myList):
    for element in myList:
        if myList.count(element) > 1:
            return False
    return True

def other_implementation(myList):
    visited_elements = []

    for element in myList:
        if element not in visited_elements:
            visited_elements.append(element)
        else:
            return False
    return True
            

print(is_unique(my_list))
print(other_implementation(my_list))
