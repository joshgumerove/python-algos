# write a function called middle that takes a list and returns a new list that contains all but the first and last elements

my_list = [1, 2, 3, 4]

def middle(lst):
    new_list = lst[:]
    return new_list[1:-1]

print(middle(my_list))
