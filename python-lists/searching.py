# SEARCHING FOR AN ELEMENT IN A LIST

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# in operator and linear search 

# in operator:

print(50 in my_list) # --> True
print(55 in my_list) # --> False

if 20 in my_list: # time complexity: O(n) --> needs to check each element one by one
    print(my_list.index(20)) # gives us the index value of the element

else: 
    print("element not found")

if 25 in my_list:
    print(my_list.index(25)) 

else: # will print this since element is not in the list
    print("element not found")

# linear search:

def search_in_list(lst, value):
    for i in lst: # also O(n) time complexity  -- space complexit of O(1) since do not need any extra memory to execute
        if i == value:
            return lst.index(value)
    return "value not in list"

print(search_in_list(my_list, 100)) # --> value not in list
print(search_in_list(my_list, 80)) # --> 7