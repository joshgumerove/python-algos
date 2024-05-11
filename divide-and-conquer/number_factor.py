def number_factor(n):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        sub_1 = number_factor(n -1)
        sub_2 = number_factor(n - 3)
        sub_3 = number_factor(n - 4)
        
        return sub_1 + sub_2 + sub_3
    
    
    
print(number_factor(5))