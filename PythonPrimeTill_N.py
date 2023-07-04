#python program to check prime till given N

number = int(input("Enter upto which number you want to print prime number: "))

list = []

for i in range(2, number+1) :
    flag = 1
    for j in range(2, i):
        if i%j == 0:
            flag = 0
            break
    if flag:
        list.append(i)

print(list)
