# finding a number in an array

import numpy as np

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def find_number(numsArray, n):
    for i in range(len(numsArray)):
        if numsArray[i] == n:
            return i
    return "number not found"

print(find_number(my_array, 8))
print(find_number(my_array, 30))