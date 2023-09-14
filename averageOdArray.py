
'''

Program to Calculate the Average of All Elements of an Array

'''

nums = [1,2,3,4,5]

def average(nums):
    sum = 0;
    for i in nums:
        sum = sum + i
    avg = sum/len(nums)
    return avg

print("Average of all elements of array is:",average(nums))

'''
Output:
Average of all elements of array is: 3.0
'''