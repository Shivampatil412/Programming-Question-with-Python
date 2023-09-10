#Python Program to Reverse a number
'''
121
121 % 10 = 1
0 * 10 + 1  = 1
121 // 10 = 12

12 % 10 = 2
1 * 10 + 2  = 12
12 // 10 = 1

1 % 10 = 1
12 * 10 + 1 = 121
'''

def reverseNum(num):
    sum = 0
    while(num !=0):
        digit = num % 10
        sum = sum * 10 + digit
        num = num // 10
    return sum

n =  int(input("Enter Number:"))
x = reverseNum(n)
print(n,"Reverse is:",x)

'''
Enter Number:101
101 Reverse is: 101
'''