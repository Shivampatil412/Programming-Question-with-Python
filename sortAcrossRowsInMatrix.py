

'''
Python Program To Sort 2D Array Across Rows
Problem Link: https://www.geeksforgeeks.org/c-program-to-sort-2d-array-across-rows/

Input:

[[8 5 7 2]
 [7 3 0 1]
 [8 5 3 2]
 [9 4 2 1]]

Output:

[[2 5 7 8]
 [0 1 3 7]
 [2 3 5 8]
 [1 2 4 9]]
'''



matrix1 = [[ 8, 5, 7, 2 ],
           [ 7, 3, 0, 1 ],
           [ 8, 5, 3, 2 ],
           [ 9, 4, 2, 1 ]];
            

            
def sortAcrossRow(matrix1):
    for i in matrix1:
        i.sort()
    return matrix1
                

print("Input Matrix:",matrix1)
print("Output Matrix:",sortAcrossRow(matrix1))

            