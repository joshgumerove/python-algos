# SLICING AND DELETING FROM A LIST

# SLICING:

my_list = ["a", "b", "c", "d", "e", "f"]
print(my_list[:2]) # printing the first 2 elements of the list
print(my_list[:]) # will print all elements from elements

my_list[:2] = ["x", "y"] # to update multiple elements at a time
print(my_list)

# DELETING ELEMENTS:

# methods: pop(), delete(), remove()

# pop() method: 

new_list = ["a", "b", "c", "d", "e", "f"]
new_list.pop(1) # will delete the second element
print(new_list) # be is removed (time consuming operation)

new_list.pop()
print(new_list) # by default will delete last element AND return it

element = new_list.pop()
print(element)

# delete() method:
# can use if do not need to save removed element

another_list = ["a", "b", "c", "d", "e", "f"]

del another_list[1] # important to remember this syntax
print(another_list)

del another_list[:2] # delete multiple elements at once
print(another_list)

# remove() method:
# helpful when know the element that want to remove (by value) 

third_list = ["a", "b", "c", "d", "e", "f"]
third_list.remove("d") # remove the given value
print(third_list)
# third_list.remove(10) will throw an error if value is not in list

