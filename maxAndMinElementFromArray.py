'''
Max and Min element from list

'''
nums = [11,54,87,999,23,45]

def maxElem(nums):
    maxNum = -999999
    for num in nums:
        if maxNum < num:
            maxNum = num
    return maxNum

def minElem(nums):
    minNum = 999999
    for num in nums:
        if minNum > num:
            minNum = num
    return minNum

print("Max Element from list is:",maxElem(nums))
print("Min Element from list is:",minElem(nums))
            
'''
Output:
Max Element from list is: 999
Min Element from list is: 11

'''