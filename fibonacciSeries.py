
'''
Fibonacci Series upto N
Fn = Fn-1 + Fn-2
'''

fn1 = 0
fn2 = 1

n = int(input("Enter Number:"))

if n < 1:
    print("Please enter a valid number greater than or equal to 1")
elif n == 1:
    print(fn1)
elif n == 2:
    print(fn2)
else:
    print(fn1)  # Print the first two Fibonacci numbers
    print(fn2)

    for i in range(2, n):
        fn = fn1 + fn2
        fn1 = fn2
        fn2 = fn
        print(fn)
