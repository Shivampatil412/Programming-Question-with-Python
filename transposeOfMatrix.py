

'''
Python program to find the transpose of a matrix. 
The transpose of a matrix is a new matrix formed by interchanging its rows with columns.
In simple words, the transpose of A[][] is obtained by changing A[i][j] to A[j][i].

Problem Link: https://www.geeksforgeeks.org/c-transpose-matrix/

Input:

[[1,2,3],
 [4,5,6],
 [7,8,9]]

Output:

[[1,4,7],
 [2,5,8],
 [3,6,9]]
 
'''

import numpy as np

matrix1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]
           
matrix2 = np.zeros_like(matrix1)          

            
def transposeMatrix(matrix1):
    for i in range(0,len(matrix1)):
        for j in range(0,len(matrix1)):
            matrix2[i][j] = matrix1[j][i]
    return matrix2

print("Input Matrix:",matrix1)
print(matrix2)
print("Output Matrix:",transposeMatrix(matrix1))

            