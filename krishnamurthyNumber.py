'''
A Krishnamurthy number is a number whose sum of the factorial of digits is equal to the number itself.
For example, 145 is the sum of the factorial of each digit.
1! + 4! + 5! = 1 + 24 + 120 = 145
'''

def fact(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact
    

def iskrishnamurthyNum(num):
    sum = 0
    temp = num
    while(num !=0): 
        digit = num % 10
        sum = sum + fact(digit)
        num = num // 10
    if temp == sum:
        return True
    else: 
        return False
 
x = iskrishnamurthyNum(40585)
if x:
     print("Yes!!!....it is Krishnamurthy Number")
else:
    print("No...it is not Krishnamurthy Number")


for i in range(1, 1000):
    x = iskrishnamurthyNum(i)
    if x:
        print(i, end = " ")
        
'''
OP:
Yes!!!....it is Krishnamurthy Number
1
2
145
'''
