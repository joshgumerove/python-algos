def first_method():
    second_method()
    print("I am the first method")
    
def second_method():
    third_method()
    print("I am the second method")

def third_method():
    fourth_method()
    print("I am the third method") # first method popped of the stack
    
def fourth_method():
    print("I am the fourth method") # does not get inserted on the stack memory

first_method() 
# first see fourth_method run
# note: stack works using LIFO

def recursive_method(n):
    if n < 1:
        print("n is less than 1")
        
    else:
        recursive_method(n -1) # does not have to be last thing in method
        print(n) # note how can print the value after calling method -- note what happens when move this up a line
        
recursive_method(4)

def fibonacci(n):
    if(n <= 2):
        return 1
    return fibonacci(n -1) + fibonacci(n -2)

print(fibonacci(10))

# note - the time and space problems presented by recursion
# note - recursion is not as fast as iteration
# can improve time complexity through memoization
