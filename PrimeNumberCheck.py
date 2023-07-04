#python program to check whether given number is prime or not

number = int(input("Enter Number: "))

flag = 1;

if(number == 1):
    print("Enter number grater than 1")
else:
    for i in range(2,number):
        if (number%i) == 0:
            flag = 0
            break
if (flag):
    print("Prime Number")
else:
    print("Not a Prime Number")