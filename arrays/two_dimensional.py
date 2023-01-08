import numpy as np


# creating 2D (lesson 1)

# representing multiple temperatures over multiple days

# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 11, 18, 14, 9

twoDArray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]
                      ]) # better time complexity to instantiate with values right away

print(twoDArray)

# insertion 2D arrays (Lesson 2)

# format must be matrix format to be recognized as 2D array

newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1) # if made axis zero would be added as a new column instead of a new row
print(newTwoDArray)

# adding to the end
newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0) # if made axis zero would be added as a new column instead of a new row
print(newTwoDArray)

# accessing elements of Two Dimensional Array (Lesson 3)

print(twoDArray[0][2]) # a[i][j] row index then column index

def access_elements(array,rowIndex, columnIndex):
    if rowIndex > len(array) -1:
        return "invalid row index"
    
    if columnIndex > len(array[0]) -1: # all have same length so can just use the first
        return "invalid columnIndex index"
    
    return array[rowIndex][columnIndex]

print(access_elements(twoDArray, 1, 2))
print(access_elements(twoDArray, 10, 1))
print(access_elements(twoDArray, 1, 10))
print(access_elements(twoDArray, 2, 1))

# Traversal of 2D array (Lesson 4)
print("traversal section")
def traverse2DArray(array):
    for i in range(len(array)): #gives the number of rows
        for j in range(len(array[0])): #not inclusive of last item in range
            print(array[i][j])
        
traverse2DArray(twoDArray)

# Searching for an element in a 2D Array (Lesson 5)
# checking if a value exists in a 2D array
# using linear search in this example

twoDArray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]])

print(twoDArray)

def search2DArray(arr, value):
    for lst in arr:
        for val in lst:
            if val == value: # note this syntax (in JS use ===)
                return True
    return False
            
print(search2DArray(twoDArray, 8))
print(search2DArray(twoDArray, 30))

#deletion from a 2D Array (Lesson 6)
# O(mn) time complexity if deleting a column or a row

newTDArray = np.delete(twoDArray, 0, axis=1)
print(newTDArray)
                