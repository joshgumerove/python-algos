# deleting an element from a dictionary
# will look at the pop() method:
    # removes a key-value pair with the given key and returns the value

my_dict = {"name": "Josh", "age": 20, "address": "London"}

name = my_dict.pop("name")
print(my_dict)
print(name)

# popitem(): removes and returns the last item 

another_dict = {"name": "Josh", "age": 20, "address": "London"}
test_value = another_dict.popitem()
print(another_dict)
print(test_value) # note that this is the key-value pair (not just the value)

# clear(): empties our dictionary

dict_3 = {"name": "Josh", "age": 20, "address": "London"}
dict_3.clear()
print(dict_3)

# del: keyword (difference in how it is called)

dict_4 = {"name": "Josh", "age": 20, "address": "London"}

del dict_4["age"]

print(dict_4)

# deleting an item from a dictionary O(1) time complexity on average
# amortized worst case O(n) in worst case
# space complexity is O(1)




    


