# list operations / functions 

# + operator: concatenates a list

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b) # --> [1,2,3,4,5,6]

# * operators: repeats the elements

c = [0]
c = c * 4
print(c) # --> [0,0,0,0]

d = [1, 2, 3]
d = d * 3
print(d) # will repeat [1, 2, 3] 3 times

# FUNCTIONS

# len function:

e = [0,1,2,3,4,5,6]
print(len(e)) # returns the number of elements in a list

# max function:

print(max(e)) # returns the largest element in the list (must have all of a certain data-type)

# min function

print(min(e)) # returns the smallest number/value in the list

# sum function

print(sum(e)) # sums up all elements in a list (only for integers)

number_list = []

while True: # will run until we manually exit
    inp = input('Enter a number: ')
    
    if inp == "done":
        break

    value = float(inp)
    number_list.append(value) # note how we had to convert the string to an integer/float
    total = sum(number_list)
    count = len(number_list)
    average = total/count
    
    print(average)
    
