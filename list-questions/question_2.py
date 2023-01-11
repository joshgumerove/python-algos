# question 2 - Two Sum:
# write a program to find all pairs of integers whose sum is equal to a given number
# pairs must be distinct

my_list = [2, 6, 3, 9, 11, 0, 4.5, 4.5] # 
other_list = [1,2,3,2,3,4,5,6]

def find_pairs(nums, target):
    pairs_list = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)): # important to remember this syntax (need to comma separate)
            pair_sum = nums[i] + nums[j]
            if nums[i] == nums[j]: # since must be distinct (alteration on leetcode question)
                continue
            if pair_sum == target:
                pairs_list.append([i, j])
    return pairs_list

print(find_pairs(my_list, 9))
print(find_pairs(other_list, 6))
                
            
            


            

    
    
        
            
        