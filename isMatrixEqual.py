

'''
Python Program to Check Whether Two Matrices Are Equal or Not
Problem Link: https://www.geeksforgeeks.org/c-program-to-check-whether-two-matrices-are-equal-or-not/

Input: 

First Matrix:   
1, 2, 3, 4
1, 2, 3, 4
1, 2, 3, 4
1, 2, 3, 4

Second matrix:
1, 2, 3, 4
1, 2, 3, 4
1, 2, 3, 4
1, 2, 3, 4

Output: 

Matrices are equal.

'''



matrix1 = [[ 1, 2, 3, 4 ],
            [ 1, 2, 3, 4 ],
            [ 1, 2, 3, 4 ],
            [ 1, 2, 3, 4 ]];
            
matrix2 =  [[ 1, 2, 3, 4 ],
            [ 1, 2, 3, 4 ],
            [ 1, 2, 3, 4 ],
            [ 1, 2, 3, 4 ]];
            
def isMatrixEqual(matrix1,matrix2):
    for i in range(0,len(matrix1)):
        for j in range(0,len(matrix2)):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    return True
                
if isMatrixEqual(matrix1,matrix2):
    print("Given Matrix are equal")
else:
    print("Given Matrix are not equal")
            