from array import * # to import everything from the module

arr_1 = array('i', [1, 2, 3])
print(arr_1)

arr_2 = array('d', [1.1, 1.2, 1.3])
print(arr_2)
print(type(arr_2))

# array insertion

arr_1.insert(3, 10)
print(arr_1)
arr_1.insert(0, 5)
print(arr_1) # every prior value moves down 1

# iterating over an array 
for element in arr_1:
    print(element)

# deleting from an array
del arr_1[0]
print(arr_1)

# insertion of element at the begining of an array --> time complexity O(N)
# insertion at the end of the array --> time complexity O(1)/constant time complexity

def traverse_array(arr):
    for element in arr:
        print(element)

traverse_array(arr_1)

print(arr_1[2])

arr_1 = [1, 2, 3, 4, 5, 6]

def access_element(array, index):
    if index > len(array) -1:
        print("Index for element not found")
    else:
        print(array[index])

# accessing an element in an array
        
access_element(arr_1, 1)
access_element(arr_1, 10)
access_element(arr_1, 5)

def other_iteration(arr):
    for index, element in enumerate(arr):
        if index % 2 == 0:
            print("skipped")
        else:
            print(arr[index])
        
other_iteration(arr_1)

# searching for a given value in an array