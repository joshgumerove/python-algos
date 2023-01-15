
# Pairs
# Write a function to find all pairs of an integer array whose sum is equal to a given number.

# Example

# pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']

def pair_sum(arr, sum):
    pair_list = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)): # since already tested previous option
            if arr[i] + arr[j] == sum:
                pair_to_string = f"{arr[i]}+{arr[j]}"
                pair_list.append(pair_to_string)
    return pair_list

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))

pr