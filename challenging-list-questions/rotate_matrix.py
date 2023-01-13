# rotate matrix 90 degrees clockwise
# NxN matrix

# [ 0  1  2  3   columns
#0  1  2  3  4
#1  5  6  7  8
#2  9 10 11 12
#3  13 14 15 16
#  ] 
# https://www.youtube.com/watch?v=JGZ04Bi-sOc


# step 1 --> transpose matrix (move every row down one) first row --> should become first column

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

def transpose_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j] = matrix[j][i]
    
    return matrix      
# [
#  [1, 5, 9, 13], 
#  [5, 6, 10, 14], 
#  [9, 10, 11, 15], 
#  [13, 14, 15, 16]
#  ]
        
# print(transpose_matrix(matrix))

# step 2 --> reverse rows after they have been transposed

def reverse_rows(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n):
            left = matrix[j][i]
            right = matrix[j][n -i - 1] # swapping 2 at a time so do not need to perform -- therefore n // 2
            matrix[j][i] = right
            matrix[j][n - i -1] = left
    return matrix
    

# print(reverse_rows(matrix))

def rotate_matrix(matrix):
    matrix_copy = matrix[:]
    transposed_matrix = transpose_matrix(matrix_copy)
    return reverse_rows(transposed_matrix)


print(rotate_matrix(matrix))    
        