def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)


custom_list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
selection_sort(custom_list)
