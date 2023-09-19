'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1

Problem Link: https://leetcode.com/problems/single-number/

we know that xor operator as ^
"a ^ a = a":

In this expression, "a" XORed with itself results in "a."
When you XOR a value with itself, the result is always 0 if "a" is 0 or 1 if "a" is 1. This is because XOR returns 0 for equal inputs and 1 for different inputs.
"a ^ 0 = 0":

In this expression, "a" XORed with 0 always results in 0.
XORing any value with 0 in Boolean algebra results in the same value because 0 XOR 0 is 0, and 1 XOR 0 is 1.
so if we ^(xor) with entire array then all repeating numbers will leading to 0 and we will get unique number.
 
time: o(n)
space : o(1)
'''

def isUnique(nums):
    ans = 0
    for num in nums:
        ans ^= num
    return ans

nums = [4,1,2,1,2] #[1,2,3,4,6,4,3,2,1]
print("Unique Element in array is:",isUnique(nums))

'''
Output:Unique Element in array is: 4
'''