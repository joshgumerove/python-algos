# remember -- dictionaries are MUTABLE

my_dict = {"name": "Eddy", "age": 26}
my_dict["age"] = 27
print(my_dict)

# note --> updating the value is O(1) time complexity (as well as the space complexity)

my_dict["address"] = "London"
print(my_dict)

# adding a pair to the dictionary --> is O(1) time complexity
# amortized O(1) space complexity

