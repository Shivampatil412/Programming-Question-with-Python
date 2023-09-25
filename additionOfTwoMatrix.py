


'''
Matrices are the collection of numbers arranged in order of rows and columns. 
In this article, we will learn to write a Python program for the addition of two matrices.

Problem Link: https://www.geeksforgeeks.org/c-matrix-addition/

Input: 
mat1 =   [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


mat2 =    [[5, 6, 1],
           [7, 2, 9],
           [6, 1, 3]]

Output:

matrix_ans = [[6,8,4],
              [11,7,15],
              [13,9,12]]

Explanation:
1+5=6, 2+6=8, 3+1=4, 4+7=11, 5+2=7, 6+9=15, 7+6=13, 8+1=9, 9+3=12 

'''
import numpy as np

matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
           
matrix2 = [[5, 6, 1],
           [7, 2, 9],
           [6, 1, 3]]
           
matrix_ans = np.zeros_like(matrix1)

for i in range(0,len(matrix1)):
    for j in range(0,len(matrix1)):
        matrix_ans[i][j] = matrix1[i][j] + matrix2[i][j]


print("Addition of Matrix1 and Matrix2 is:\n",matrix_ans)



