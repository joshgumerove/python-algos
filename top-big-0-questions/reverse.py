def reverse(arr):
    for i in range(0, int(len(arr)/2)):
        other = len(arr)-i-1
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp
    print(arr)

reverse([2, 4, 6, 7])

# big O(N/2)
        
