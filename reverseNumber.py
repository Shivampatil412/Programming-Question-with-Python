#Python Program to Reverse a number

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