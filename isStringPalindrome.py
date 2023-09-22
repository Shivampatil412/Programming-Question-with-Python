
'''
A string is said to be palindrome if the reverse of the string is the same as the string. 
For example, “abba” is a palindrome because the reverse of “abba” will be equal to “abba”
so both of these strings are equal and are said to be a palindrome, but “abbc” is not a palindrome.

Problem Link: https://www.geeksforgeeks.org/c-program-check-given-string-palindrome/

Input: 'abbba'
Output: "String is Palindrome"

Input: 'abbca'
Output: "String is not Palindrome"

'''



strng = 'abbca'
left = 0
right = len(strng) - 1

def isPalindrome(strng,left,right):
    while(left < right):
        if strng[left] != strng[right]:
            return False
        left += 1
        right -= 1
    return True
            
if isPalindrome(strng,left,right):
    print("String is Palindrome")
else:
    print("String is not Palindrome")
