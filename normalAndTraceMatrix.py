
'''
Python program to find the normal and trace of a matrix. Below are the examples:

Problem Link: https://www.geeksforgeeks.org/c-program-to-find-normal-and-trace-of-matrix/

input: mat[][] = {{1, 2, 3},
                 {4, 5, 6},
                 {7, 8, 9}};
Output: 

Normal = 16
Trace  = 15

Explanation: 

Normal = sqrt(1*1+ 2*2 + 3*3 + 4*4 + 5*5 + 6*6 + 7*7 + 8*8 + 9*9) = 16
Trace  = 1+5+9 = 15

Input: mat[][] = {{5, 6, 1},
                  {7, 2, 9},
                  {6, 1, 3}};
Output:

Normal = 10
Trace  = 10

Explanation:

Normal = sqrt(5*5+ 6*6 + 1*1 + 7*7 + 2*2 + 9*9 + 6*6 + 1*1 + 3*3) = 15
Trace  = 5+2+3 = 10

'''

matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]];
           
normal = 0
trace = 0

for i in range(0,len(matrix1)):
    for j in range(0,len(matrix1)):
        normal = normal + matrix1[i][j] * matrix1[i][j]

normal = int(normal ** 0.5)
        
        
print("Normal:",normal)

for i in range(0,len(matrix1)):
    trace = trace + matrix1[i][i]

print("Trace:",trace)

