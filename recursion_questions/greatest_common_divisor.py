def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)

print(greatest_common_divisor(12, 24))
print(greatest_common_divisor(8, 12))
print(greatest_common_divisor(1, 7))
print(greatest_common_divisor(7, 7))

# greatest common divisor of two numbers
# 1. recursive case - the flow

# larget positive integer that divides the numbers without a 
# gcd(8, 12) =4