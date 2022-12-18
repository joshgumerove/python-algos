def power_of_two(n):
    if n == 0:
        return 1
    else:
        power = power_of_two(n -1)
        return power * 2
    
print(power_of_two(3))

# 0 = 1
# 1  * 2 = 2
# 2 * 2 = 4
# 4 * 2 = 8

def power_of_2(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power

print(power_of_2(2))