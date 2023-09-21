
'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Problem Link: https://leetcode.com/problems/number-of-good-pairs/description/ 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
'''
nums = [1,2,3,1,1,3]
 
def numIdenticalPairs(nums):
    sample = {}
    res = 0
    for num in nums:
        if num in sample:
            res = res + sample[num]
            sample[num] = sample[num] + 1
        else:
            sample[num] = 1
    return res

print(numIdenticalPairs(nums))
     
'''     
    1 ->     res = 0 samp[1] = 1
    2 ->     res = 0 samp[2] = 1
    3 ->     res = 0 samp[3] = 1
    1 ->(already Present) res = 0 + samp[1] = 0+1 = 1 samp[1] = samp[1]+1 => samp[1] = 2
    1 ->(already Present) res = 1 + samp[1] = 1+2 = 3 samp[2] = samp[2]+1 => samp[1] = 3
    3 ->(already Present) res = 3 + samp[3] = 3+1 = 4 samp[3] = samp[3]+1 => samp[3] = 2
     therefore return res = 4
'''