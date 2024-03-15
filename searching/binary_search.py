import math


def binary_search(arr, val):
    start = 0
    end = len(arr) - 1
    middle = math.floor((start + end) / 2)

    while arr[middle] != val and end >= 0:
        if val < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)
        print(start, middle, end)
    return middle

# better performacne than linear search (if list is sorted already)
# only works with sorted lists (limitation)


list1 = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binary_search(list1, 17))
