arr = [1, 2, 3, 5, 10, 12]

# constant time O(1)

print(arr[3], "constant time")

# linear time O(N)

for element in arr: 
    print(element, "linear time") 
                        # should attemet to keep algorithms linear or constant if possible


array = [1, 2, 3, 4, 5, 6, 7, 8]

# logarithmic time

for index in range(0, len(array), 3):
    print(array[index], "log time")     # only logs at certain levels (index 0 and 3) -- every third element
                                        # does not pass through every item (so does not have linear time)
                                        
# quadratic time
                                        
for x in array:
    for y in array:
        print(x, y, "quadratic time")   # visiting every element twice in the array
        


# exponential time complexity

def fibonacci(n):
    if n <= 1:
        return n                                             

    return fibonacci(n-1) + fibonacci(n-2)
                                        
print(fibonacci(10), "exponential time")                                        
                                        


