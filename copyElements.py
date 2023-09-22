
'''
copy all the elements of one array to another in Python

Problem Link: https://www.geeksforgeeks.org/c-program-to-copy-all-the-elements-of-one-array-to-another-array/

Input: 

First Array:  a[5] = {3, 6, 9, 2, 5} 

Output: 

First Array : a[5] = {3, 6, 9, 2, 5}
Second Array : b[5] = {3, 6, 9, 2, 5}
'''



nums1 = [3, 6, 9, 2, 5] 

def copyElements(nums1):
    nums2 = []
    for i in nums1:
        nums2.append(i)
    return nums2

print(copyElements(nums1))
    
