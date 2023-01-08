def printPairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

arr = [2, 4 , 6, 8]

printPairs(arr) # will print every pair in the arr

# time complexity O(N^2)