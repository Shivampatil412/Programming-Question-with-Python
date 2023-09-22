
'''
To merge 2 arrays in python

Problem Link: https://www.geeksforgeeks.org/c-program-to-merge-two-arrays/
Input:

arr1 = [1, 2, 3, 4, 5] 
arr2 = [6, 7, 8, 9, 10] 
Output: 

arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''



nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]



def mergeTwoArrays(nums1, nums2):
    nums1 = nums1 + nums2
    return nums1

merged_result = mergeTwoArrays(nums1, nums2)
print(merged_result)
