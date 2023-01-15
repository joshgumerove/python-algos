# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

def first_second(score_list):
    new_score_list = score_list[:]
    new_score_list.sort()
    
    return new_score_list[-1], new_score_list[-2]

print(first_second(myList))
    


