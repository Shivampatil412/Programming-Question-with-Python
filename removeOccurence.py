
'''
To remove all the occurrences of an element in an array in Python

Problem Link: https://www.geeksforgeeks.org/c-program-to-remove-all-occurrences-of-an-element-in-an-array/
Input:

array = [1, 2, 1, 3, 1] 
value = 1

Output: 
array = [2, 3]
 
'''



array = [1, 2, 1, 3, 1] 
value = 1



def removeOccurence(array,value):
    ans = []
    for i in array:
        if i != value:
            ans.append(i)
    return ans

print(removeOccurence(array,value))
    
