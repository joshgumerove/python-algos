# list pitfalls (drawbacks)

my_list = [2, 4, 3, 1, 5, 7]

my_list = my_list.sort()

print(my_list) # will print none (because of sort return value)

new_list = [2, 4, 3, 1, 5, 7]
new_list.append(10)
print(new_list)

# new_list.sort() # is a mutating method (but will return None)
# print(new_list) # should copy the list before mutating so do not alter 
print(sorted(new_list)) # does not mutate