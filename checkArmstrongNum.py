
'''
A number is Armstrong Number if:
xyz.....n = x^n + y^n + z^n
153 is an Armstrong number of 3 digits, since the sum of cubes of each digit is equal to the number itself. As shown below: 

1*1*1 + 5*5*5 + 3*3*3 = 153

1634 is an Armstrong number of 4 digit, the sum of 4th power of each digit is equal to the number itself. As shown below:

1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
'''

number =  int(input("Enter Number:"))

temp = number
original_num = number
len = 0

while(original_num!=0) :
    original_num = original_num // 10
    len = len +1

def isArmstrong(number):
    sum = 0
    while(number > 0 ):
        digit = number % 10
        sum = sum + (digit**len)
        number = number // 10
    if temp == sum:
        return True
    else:
        return False

    
var = isArmstrong(number)
      
if (var):
    print("It is Armstrong number")
else:
    print("It is not not Armstrong number")
    
    
'''
4-Digit Armstrong Numbers:

1634
8208
9474
5-Digit Armstrong Numbers:

54748
92727
93084
'''