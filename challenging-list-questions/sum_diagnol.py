# Given 2D list calculate the sum of diagonal elements.
myList2D= [
    [1,2,3],
    [4,5,6],
    [7,8,9]] 


def sum_diagnol(a):
    diagnol_sum = 0
    for i in range(len(a)):
        diagnol_sum += a[i][i] # correct logic
    return diagnol_sum

print(sum_diagnol(myList2D))


            

