# how to find an element in a dictionary 
# will do a linear search

my_dict = {"name": "Josh", "age": 20, "address": "London"}

def search_dictionay(dictionary, value):
    for key in dictionary:
        if my_dict[key] == value:
            return {key: value}
    return False

print(search_dictionay(my_dict, 20))