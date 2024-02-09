def bubble_sort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):  # decrease number of loops as
            if customList[j] > customList[j + 1]:
                customList[j], customList[j +
                                          1] = customList[j + 1], customList[j]
    print(customList)


# compare adjacent elements
# note how move from pair to pair
# numbers go to right edge (bubble up)

list1 = [2, 1, 7, 6, 5, 3, 4, 8]
bubble_sort(list1)
