# different methods

# clear(): does not take any parameters or return a value
my_dict = {"name": "Josh", "age": 20, "address": "London"}
my_dict.clear()
print(my_dict)

# copy(): returns a shallow copy of the dictionary
dict2 = {"name": "Josh", "age": 20, "address": "London"}
dict3 = dict2.copy() # returns a shallow copy here
print(dict3) # made a copy of dict2

# fromkeys(): creates a new dictionary from given sequence of elements with value provided by the user
dict4 = {}.fromkeys([1, 2, 3], 0) # useful method for alogrithms
print(dict4)

# get(): returns the value of a key if the key is in a dictionary

print(dict2.get("name"))
my_name = dict2.get("name", "no name in dictionary") # returns the value
print(my_name)

# items(): returns a view object that displays a list of dictionaries, key value tuple pairs
for key, value in dict2.items():
    print(key)
    print(value)

print(dict2.items())

# keys(): displays a list of keys in view object (returns list of keys)

print(dict2.keys())

# setdefault(): returns the value of a key if it is in the dictonary otherwise sets value to value provided
print(dict2.setdefault("name", "Steven"))
print(dict2.setdefault("school", "harvard")) # gets inserted if the value does not exist (if not provided will defualt to none)
print(dict2)

# values(): returns a list of values in the dictonary
print(dict2.values())

# update(): updates the dictionary with the elements from another dictionary or from an iterable of key-value pairs
dict5 = {"youngest": "Josh", "middle": "Jeremy", "oldest": "Brennan"}
dict6 = {"grandma": "katherine", "grandpa": "Harvey", "youngest": "Joshua"}
dict5.update(dict6) # note that the return value is none however (but will still update the dictionary)
print(dict5)