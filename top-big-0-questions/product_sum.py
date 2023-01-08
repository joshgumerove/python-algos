def foo(array):
    sum = 0
    product = 1
    
    for i in array:
        sum += i

    for i in array:
        product *= i

    print(f"Sum = {str(sum)}, Product = {str(product)}")
    
foo([1, 2, 3])

# time complexity O(N)