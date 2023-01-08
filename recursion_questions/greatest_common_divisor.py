def greatest_common_divisor(a, b):
    assert int(a) == a and int(b) == b, "both numbers must be integers"
    if a < 0:
        a = -1 * a

    if b < 0:
        b = -1 * b
        
    if b == 0:
        return a # note how can perform logic before base case
    return greatest_common_divisor(b, a % b)

print(greatest_common_divisor(12, 24))
print(greatest_common_divisor(8, 12))
print(greatest_common_divisor(1, 7))
print(greatest_common_divisor(7, 7))
print(greatest_common_divisor(-12, -24))
# print(greatest_common_divisor(7.5, 4))

# greatest common divisor of two numbers
# 1. recursive case - the flow

# larget positive integer that divides the numbers without a 
# gcd(8, 12) =4
# note the use of euclidian algorithm