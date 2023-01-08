# updating and inserting into python list

myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)

myList[2] = 33 # O(1) time complexity (very efficient)
print(myList)

# methods: insert(), append(), extend()

myList.insert(0, 11) # all elements must now move one step to the right (time consuming operation)
print(myList)

myList.insert(4, 15)
print(myList)

# add to the end

myList.append(55) # efficient way to add an element
print(myList)

# adding a list to an existing list
newList = [11, 12, 13, 14]

myList.extend(newList) # O(n) time complexity (depends on the amount of elements in the list we are adding) 
# also O(n) space complexity

