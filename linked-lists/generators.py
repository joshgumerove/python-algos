my_family = ["Josh", "Jeremy", "Brennan"]

def test_generator(lst):
    for i in range(len(lst)):
        yield lst[i]
    
for name in test_generator(my_family):
    print(name + " Gumerove")
        