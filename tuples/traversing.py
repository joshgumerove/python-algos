tuple1 = ("a", "b", "c", "d", "e")

for i in range(len(tuple1)):
    print(tuple1[i])
    
for character in tuple1: 
    print(character)
    
# searching for an element in a tuple

print("a" in tuple1) # will return true (note time complexity: O(N))

# index() method:
print(tuple1.index("c")) # will raise error if not in tuple

if "c" in tuple1:
    print(tuple1.index("c"))


