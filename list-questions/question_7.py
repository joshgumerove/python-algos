# Rotate Matrix

# given an image represented by an NxN matrix write a method to rotate the image by 90 degrees
# 1 2 3       7 4 1
# 4 5 6  -->  8 5 2
# 7 8 9       9 6 3

import numpy as np

matrix =  np.array([
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
 ])

print(matrix)

def rotate_matrix(matrix):
    n = len(matrix)      # gives number of rows
    for layer in range(n // 2):  # will take the floor of the division
        first = layer 
        last = n - layer - 1   # 3 - 0 - 1
        for i in range(first, last):
            # save top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # move bottom element to 
            matrix[-i-1][layer] = matrix[-layer -1][-i -1]
            # move right to bottom
            matrix[-layer - 1][-i -1] = matrix[i][-layer -1]
            # move top to right
            matrix[i][-layer -1] = top
    return matrix

        
        
print(rotate_matrix(matrix))

def rotate(matrix):
    matrix_length = len(matrix)
    for matrix_list in len(matrix_length // 2):
        first_matrix = matrix_list
        last_matrix = matrix_length - matrix_list -1
        for i in range(first_matrix, last_matrix):
            pass
            
    
    
