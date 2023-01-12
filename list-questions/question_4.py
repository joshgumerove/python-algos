# Max product of two integers

import numpy as np

my_array = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])
print(my_array)

# def find_max_product(numsArray):
#     max_product = 0
    
#     for i in range(1, len(numsArray)):
#         current_product = numsArray[i] * numsArray[i - 1]
#         if current_product > max_product:
#             max_product = current_product
#     return max_product

def find_max_product(numsArray):
    max_product = 0
    
    for i in range(len(numsArray)):
        for j in range(i + 1, len(numsArray)):
            current_product = numsArray[i] * numsArray[j]
            if current_product > max_product:
                max_product = current_product
                pairs = [numsArray[i], numsArray[j]]
    print(pairs)
    return max_product
   

print(find_max_product(my_array))
    
    



