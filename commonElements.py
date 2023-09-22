
'''
Given two arrays we have to find common elements in them using Python

Problem Link: https://www.geeksforgeeks.org/c-program-to-find-common-array-elements-between-two-arrays/

Input: 

array1[] = {8, 2, 3, 4, 5, 6, 7, 1}
array2[] = {4, 5, 7, 11, 6, 1}
Output:

Common elements are: 4 5 6 7 1 
'''



nums1 = [8, 2, 3, 4, 5, 6, 7, 1] 
nums2 = [4, 5, 7, 11, 6, 1]



def commonElements(nums1,nums2):
    for i in nums1:
        for j in nums2:
            if i == j:
                print(i,end = " ")

commonElements(nums1,nums2)
    
