# question 1- missing number:

                                                    # can solve by calculating the sum of n series of :
                                                    #  1 + 2 + 3 + ... +n = n (n + 1) / 2

my_list = [1, 2, 3, 4, 5, 6, 7, 9, 10]
def find_missing_number(numList, n):
    sum_1 = n * (n + 1)/2                           # note how we implemented the equation above
    return sum_1 - sum(numList)

print(find_missing_number(my_list, 10))
    


