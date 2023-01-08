def to_binary(n):
    assert int(n) == n, "The parameter must be an integer"
    if n == 0:
        return 0
    
    return n % 2 + 10 * to_binary(int(n / 2))


# how to convert a number from decimal to binary using recursion
# 1. recursive case
# divide the number by 2
# get the integer quotient for the next iteration (result of dividing one number by another)
# get the remainder for the binary digit (quotient - result of division)

print(to_binary(10))
print(to_binary(13))
print(to_binary(12.5))