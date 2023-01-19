# tuples:
# are immutable
# are comparable and hashable
# hashable --> if has value that remains the same in its life time

# create tuple
tuple1 = "a", "b", "c"
print(type(tuple1))
print(tuple1)

tuple2 = (1, 2, 3) # advisable to include () when creating a tuple although not required
print(type(tuple2)) 
print(tuple2)

# tuple() function to create tuple

tuple3 = tuple("abc")
print(tuple3) # ('a', 'b', 'c') each is considered a separate element

# time complexity of creating a tuple --> O(1) and space complexity is O(N)
