
'''
Armstrong Number is:
xyz.....n = x^n + y^n + z^n
153 is an Armstrong number of 3 digits, since the sum of cubes of each digit is equal to the number itself. As shown below: 

1*1*1 + 5*5*5 + 3*3*3 = 153

1634 is an Armstrong number of 4 digit, the sum of 4th power of each digit is equal to the number itself. As shown below:

1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634
'''


def digitLen(num):
    len = 0
    while(num!=0) :
        num = num // 10
        len = len +1
    return len

def isArmstrong(number):
    sum = 0
    temp = number
    leng = digitLen(number)
    while(number > 0 ):
        digit = number % 10
        sum = sum + (digit**leng)
        number = number // 10
    if temp == sum:
        return True
    else:
        return False


for i in range(10,100000):    
    var = isArmstrong(i)
    if (var):
        print(i, end = " ")

    
    
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