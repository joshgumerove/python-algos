# measurement of the amount of storage (memory) and algorithm 


# array of size n: O(n)
arr_1 = [1, 2, 3]

# array of size n * n: O(n^2)
arr_2 = [[1, 2], [3, 4]]

# recursion and space complexity
def sum(n):
    if n <= 0:
        return 0
    return n + sum(n -1) # count in the space stack to determine space complexity (space complexity grows in this case linearly with input)
    
print(sum(3))

# space complexity: O(1)
def pair_sum_sequence(n):
    sum = 0
    for i in range(0, n+1):
        sum = sum + pair_sum(i, i + 1) # not a recursive call (therefore not adding any layer to the memory stack)
    return sum

def pair_sum(a, b):
    return a + b