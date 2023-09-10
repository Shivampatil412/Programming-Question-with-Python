'''
Palindrome number refers to those number which is equal to the reverse of that
number.Palindrome word refers to any data which is equal to its reverse.The data
is either a number, a string, a word, etc.

Input:  Number = 12321 
Output: Given number is a Palindrome number.
Explanation : reverse of number is 12321 which is equal to original number

Input: Number = 1232
Output: Given number is not a Palindrome number.
Explanation : reverse of number is 2321 which is not equal to original number
'''

def isPalindrome(num):
    temp = num
    sum = 0
    while(temp !=0):
        digit = temp % 10
        sum = sum * 10 + digit
        temp = temp // 10
    if sum == num:
        return True
    else:
        return False
    
num = int(input("Enter Number:"))    
x = isPalindrome(num)
if x:
    print(num,"is Palindrome Number")
else:
    print(num,"is not a Palindrome Number")
    

'''
OP:
Enter Number:12321
12321 is Palindrome Number
'''