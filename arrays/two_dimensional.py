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
                      [11, 18, 14, 9]
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