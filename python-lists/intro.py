# built-in data structure
# holds an ordered collection of items

# accessing/traversing a list

shoppingList = ["Milk", "Cheese", "Butter"]

print(shoppingList[2]) # ---> Butter

for i in range(len(shoppingList)):
    print(shoppingList[i])
    
print("Milk" in shoppingList) # --> True
# note the in operator
print("Bread" not in shoppingList)
print("Bread" in shoppingList)

for item in shoppingList:
    print(item) # do not need to use range(len(shoppingList))
    
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + " in cart" # need to use index if want to change value when iterating over
    
print(shoppingList)

emptyList = []

for item in emptyList:
    print(item) # this code will never run