def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n -1)



print(factorial(4))
print(factorial(10))




# product is the result of multiplication
# only for positive numbers
# factorial of zero is 
# representation: 4! = 4 * 3 * 2 * 1



# 3 steps for writing recursion
# first: recursive case - the flow