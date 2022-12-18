def fib(n):
    assert n >= 0 and int(n) == n, "number must be positive"
    if n <= 1: # if n <= 2 return 1
        return n
    
    return fib(n-1) + fib(n-2)


print(fib(10))
print(fib(3))
print(fib(6))
# print(fib(1.5))
# print(fib(-10))
# sequence of numbers in which number is sum of two previous numbers