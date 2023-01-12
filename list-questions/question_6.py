# permutation
# given two lists write method to determine if one is permutation of another

def list_is_permutation(list_1, list_2):
    first_list = list_1[:]
    second_list = list_2[:]
    if len(first_list) != len(second_list):
        return False
    first_list.sort() 
    second_list.sort()
    
    return first_list == second_list                                # note that we can compare lists


    # for i in range(len(first_list)):
    #     if first_list[i] != second_list[i]:
    #         return False
    # return True

print(list_is_permutation([1, 3, 2], [3, 2, 1]))

