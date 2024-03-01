import math


def insertion_sort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList


def bucket_sort(customList):
    number_of_buckets = round(math.sqrt(len(customList)))


list1 = [2, 1, 7, 6, 5, 3, 4, 8]
bucket_sort(list1)
