'''
Given a number (num)  we need to check whether it is a Neon Number ( i.e. a number where the sum of digits of the square 
of the number is equal to the number )
num = 9
square of 9 is 9 * 9 = 81 , sum of digit of square is 8 + 1 = 9 (i.e equal to given number).
num = 10
Square of 10 is 10 * 10 = 100 , sum of digit of square is 1 + 0 + 0 = 1 (i.e. not equal to given number).

'''

def isNeon(num):
    square =  num * num
    sum = 0
    while(square !=0):
        digit = square % 10
        sum = sum + digit
        square = square // 10
    if num == sum:
        return True
    else:
        return False


for i in range(0, 1000):
    x = isNeon(i)
    if x:
        print(i, end = " ")