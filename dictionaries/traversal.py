# traversing through a dictionary

my_dict = {"name": "eddy", "age": 26, "address": "London"}

# traversing --> visiting all pairs in the dictionary one by one

def traverse_dict(dict):
    for key in dict:
        print(key, dict[key])
        
traverse_dict(my_dict)

# traversing a dictonary has O(n) time complexity and O(1) space complexity