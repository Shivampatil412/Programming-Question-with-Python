
'''

Program to Find the Sum of Fibonacci Numbers at Even Indexes up to N Terms

'''
n = int(input("Enter Number:"))

def fibEvenSum(n):
    nums = [0,1]
    sum = 0
    for i in range(2, 2*n+1):
        nums.append(nums[-1] + nums[-2])
    print(nums)
    for i in range(0,len(nums)):
        if i % 2 == 0:
            sum = sum + nums[i]
    return sum
    
print(f"The sum of Fibonacci numbers at even indexes up to {n} terms is:",fibEvenSum(n))
'''
Output:
Enter Number:5
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
The sum of Fibonacci numbers at even indexes up to 5 terms is: 88
'''