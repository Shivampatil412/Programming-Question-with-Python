'''
Python Program to detect even odd number without using Modulo operator
do n&1 == 1
lets say n = 19
n in binary is 100101
when we add any number in binary 1 + 1 = 0 and carry is one
in when we and it 1 & 1 is 1
Therefore 1 0 0 1 0 1
        & 0 0 0 0 0 1
        ______________
          0 0 0 0 0 1
          
as we got 000001 => 1 so its odd number otherwise even
'''

def isOdd(n):
    return n & 1 == 1

for i in range(0, 101):
    if isOdd(i):
        print(i,"is Odd Number")
    else:
        print(i, "is Even Number")