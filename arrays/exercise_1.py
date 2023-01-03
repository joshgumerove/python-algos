from array import *

#create an array and traverse
first_array = array("i", [1, 2, 3, 4])

for element in first_array:
    print(element)
    
#access individual elements throught indexes
second_element = first_array[1]
print(second_element)

#append value to the end of the array
first_array.append(20)
print(first_array)

#insert value in array using the insert method
first_array.insert(2, 35)
print(first_array)

#extend python array using the extend method

first_array.extend([4, 8, 16, 32])
print(first_array)

#add items from list into array using the fromlist method
first_array.fromlist([10, 20, 30])
print(first_array)

#remove any array element using remove() method
first_array.remove(10)
print(first_array)

#reverse the array using reverse() method
first_array.reverse() #mutates the original array
print(first_array)

#get array buffer information trhough buffer_info() method
print(first_array.buffer_info())

#check number of occurents of element in array using count method
print(first_array.count(4))

#convert array to string using tostring() method
print(first_array.tostring())

#convert array to list
new_list = first_array.tolist()
print(type(new_list))

#slice array
print(first_array[0:3])
