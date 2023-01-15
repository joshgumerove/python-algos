# dictionary is an unordered collection

# first method: dict function

my_dict = dict()
print(my_dict)

# second method:

second_dict = {}

english_to_spanish = {
    "one": "uno",
    "two": "dos",
    "three": "tres"
}

print(english_to_spanish["two"])
# note: the order of elements does not matter (in terms of accessing the values)

# will get an error if try to access a key-value pair that does not exist with the method above


