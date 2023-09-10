'''
Factors of a number are the positive integers that divide the number without
leaving a remainder. For example, for n = 10, the factors will be 1, 2, 5 and 10.
'''
num = int(input("Enter Number:"))

for i in range(1, num+1):
    if num % i == 0:
        print(i, end =" ")
        
'''
OP:
Enter Number:50
1 2 5 10 25 50 
'''