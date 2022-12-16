def first_method():
    second_method()
    print("I am the first method")
    
def second_method():
    third_method()
    print("I am the second method")

def third_method():
    fourth_method()
    print("I am the third method")
    
def fourth_method():
    print("I am the fourth method")

first_method() 
# first see fourth_method run