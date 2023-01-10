import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
print(my_array)
print(my_array/2) # would not work with a python list
print(type(my_array))



data = [
    [[1, 2], [3, 4]], 
    [[5, 6], [7, 8]]
    ] # note that there are two separate nested arrays
def fun(m):
    v = m[0][0]
    print("what is v", v)
 
    for row in m:
        print(row, "is row")
        for element in row:
            print(element, "is element")
            if v < element: v = element
 
    return v
print(fun(data[0]))
# test questionis
fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

print(fruit_list1)
print(fruit_list2)

arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop()) # going through each array