def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(arrayA[i], arrayB[j])
                
printUnorderedPairs([2, 4, 6, 8], [4, 6, 8, 10])

# time complexity O(xy)
# note that this is not linear time complexity