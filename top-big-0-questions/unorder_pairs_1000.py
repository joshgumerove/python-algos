def print_unordered_pairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100):
                print(arrayA[i], arrayB[j])
                
print_unordered_pairs([2, 4, 6], [8, 10, 12])


# time complexity O(n*m*100)