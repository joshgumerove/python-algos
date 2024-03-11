def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


list_1 = [3, 5, 0, 6, 2, 1, 4]
print(pivot(list_1, 0, len(list_1) - 1))
print(list_1)

# [3, 0, 5, 6, 2, 1, 4] 1
# [3, 0, 2, 6, 5, 1, 4] 2
# [3, 0, 2, 1, 5, 6, 4] 3
# [1, 0, 2, 3, 5, 6, 4] 3 last swap
