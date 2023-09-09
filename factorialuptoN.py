'''
Python Program for factorial upto n
n! = n * (n-1) * (n-2) * (n-3)....1
'''

n = int(input("Enter Number:"))



for i in range(1,n+1):
    fact = 1
    for j in range(2,i+1):
        fact = fact * j
    print(i,"Factorial is:",fact)

'''
Enter Number:5
1 Factorial is: 1
2 Factorial is: 2
3 Factorial is: 6
4 Factorial is: 24
5 Factorial is: 120
'''