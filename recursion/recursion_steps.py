def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer only"
    
    if n == 0: #if n in [0, 1]
        return 1

    return n * factorial(n -1)



print(factorial(4))
print(factorial(10))
print(factorial(3))
print(factorial(-10))
# print(factorial(1.5))



# product is the result of multiplication
# only for positive numbers
# factorial of zero is 
# representation: 4! = 4 * 3 * 2 * 1



# 3 steps for writing recursion
# first: recursive case - the flow
# two: base case - the stopping criterion
# three: consider edge cases