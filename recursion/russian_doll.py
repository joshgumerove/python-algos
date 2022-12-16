def open_russian_doll(doll):
    if doll == 1:
        print(doll)
        print("all dolls are opened")

    else:
        print(doll)
        open_russian_doll(doll - 1)
        

print(open_russian_doll(7))

# why we need recursion:
# helps break down big problems into smaller problem
# recursive code is easier to write at times
# however are situations where iterative code is faster
# if can divide problem into similar sub-problems -- can usually use recursion

# condition:
# a method calls itself
# exit from the infinite loop


# def recursion_method(parameters):
#     if exit from condition satisfied:
#         return some value 
#     else: 
#         recursion_method(modified parameters)
