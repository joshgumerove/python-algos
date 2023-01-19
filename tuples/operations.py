# tuple operations/functions:

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 6, 9, 8, 7)

print(tuple1 + tuple2) # concatenates two tuples together
print(tuple1 * 4) # will repeat each element 4 times

print(tuple2.count(8))
print(tuple2.count(100))
print(len(tuple2))
print(tuple2.index(8))
print(max(tuple2))
print(min(tuple2))
print(tuple([1, 2, 3])) # convert list to tuple

init_tuple_a = 1, 2
init_tuple_b = (3, 4)

print("*****")
 
[print(sum(x)) for x in [init_tuple_a + init_tuple_b]] # only one tuple

