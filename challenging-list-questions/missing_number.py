# Write a function to find the missing number in a given integer array of 1 to 100.

number_list = [1, 2, 3, 4, 6]

def missing_number(num_list, n):
    total = n * (n + 1) / 2
    return total - sum(num_list)

print(missing_number(number_list, 6))

