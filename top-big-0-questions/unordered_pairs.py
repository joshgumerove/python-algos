def print_unordered_pairs(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            print(arr[i], arr[j])

arr = [2, 4, 6, 8]
print_unordered_pairs(arr)

# O(N^2)
# note how the above simplifies to quadratic time complexity