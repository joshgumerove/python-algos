def find_lcs(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + find_lcs(s1, s2, index1 + 1, index2 + 1)
    else:
        op_1 = find_lcs(s1, s2, index1, index2 + 1)
        op_2 = find_lcs(s1, s2, index1 + 1, index2)
        return max(op_1, op_2)
    
print(find_lcs("elephant", "eretpat", 0, 0))