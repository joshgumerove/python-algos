def sum_of_digits(n):
    assert n > 0 and int(n) == n, "number must be positive whole number"
    if n < 10:
        return n
    return int(n%10) + sum_of_digits(int(n/10))

print(sum_of_digits(11))
print(sum_of_digits(133))  
print(sum_of_digits(4))  
print(sum_of_digits(12))
# print(sum_of_digits(-5))
# print(sum_of_digits(8.5))


# how to find sum of digits of a positive integer number using recursion
# 1. recursive case - the flow
# note how we can get the digits by dividing by 10