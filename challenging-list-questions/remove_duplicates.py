# Duplicate Number
# Write a function to find the duplicate number on given integer array/list.

# Example

# removeDuplicates([1, 1, 2, 2, 3, 4, 5])
# Output : [1, 2, 3, 4, 5]

def remove_duplicates(arr):
    filtered_list = []

    for element in arr:
        if element not in filtered_list:
            filtered_list.append(element)
    return filtered_list

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))