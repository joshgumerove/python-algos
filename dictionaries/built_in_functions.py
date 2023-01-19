# built in methods/operations on dictionaries

my_dict = {"one": "uno", "two": "dos", "three": "tres", "four": "cuatro"}

# in operator: whether an element exists in a collection or not

print("one" in my_dict) # returns True O(1) time complexity
print("uno" in my_dict) # returns False (does not check values)
print("uno" in my_dict.values()) # True O(N) time complexity

for key in my_dict:
    print(key) # will print each key (by visiting each pair) -- this also has O(N) time complexity

# all method (returns true when all elements in iterable are true)

dict2 = {1: True, 2: True}
print(all(dict2)) # since all values are true
print(all(my_dict)) # since all values are truthy

dict3 = {1: False, 2: False}
print(all(dict3))

dict4 = {1: False, 2: True}
print(all(dict4))

list1 = [True, False]
print(all(list1)) # not working the way expected for dictionaries

# any(): returns True if any element is True

print(any(dict3))
print(any(list1))

# len(): returns the amount of items in a collection (for dictionary will return the # of pairs)

print(len(dict3))

# sorted(): returns a a sorted list from the items in an iterable
print(sorted(dict4)) # will sort the keys
print(sorted(dict4, reverse=True)) # if want to do the reverse order