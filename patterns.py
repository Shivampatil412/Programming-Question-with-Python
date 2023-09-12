

n = int(input("Enter Number:"))

'''
Pattern 1:
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''

def pattern1(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("*",end = " ")
        print()

'''
Pattern 2:

* 
* * 
* * * 
* * * * 
* * * * * 
'''

def pattern2(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*",end = " ")
        print()
        
'''
Pattern 3:
* * * * 
* * * 
* * 
*
'''

def pattern3(n):
    for i in range(1, n+1):
        for j in range(1,n+1-i):
            print("*",end = " ")
        print()
        
'''
Pattern 4:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

def pattern4(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j,end = " ")
        print()
        
'''
Pattern 5:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''

def pattern5(n):
    for row in range(1,2*n):
        cols = 2*n - row + 1 if row > n else row + 1
        for j in range(1, cols):
            print("*",end = " ")
        print()
        
'''
Pattern 6:
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    * 
'''

def pattern6(n):
    for row in range(1,2*n):
        cols = 2*n - row + 1 if row > n else row + 1
        noOfSpaces = n + 1 - cols 
        for k in range(1, noOfSpaces+1):
            print(end = " ")
        for j in range(1, cols):
            print("*",end = " ")
        print()

'''
Pattern 7:
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
'''

def pattern7(n):
    for row in range(1,n+1):
        spaces = n + 1 - row
        for space in range(1,spaces):
            print(end = "  ")
        for col in range(row, 0, -1):
            print(col,end = " ")
        for col in range(2, row+1):
            print(col, end = " " )
        print()
    
'''
Pattern 7:
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
  4 3 2 1 2 3 4
    3 2 1 2 3
      2 1 2
        1
'''

def pattern8(n):
    for row in range(1,2*n):
        cols = 2*n - row  if row > n else row
        spaces = n + 1 - cols
        for space in range(1,spaces):
            print(end = "  ")
        for col in range(cols, 0, -1):
            print(col,end = " ")
        for col in range(2, cols+1):
            print(col, end = " " )
        print()
        
'''
Pattern 9:
4 4 4 4 4 4 4  
4 3 3 3 3 3 4   
4 3 2 2 2 3 4   
4 3 2 1 2 3 4   
4 3 2 2 2 3 4   
4 3 3 3 3 3 4   
4 4 4 4 4 4 4 

take left, right, up and down
suppose take 1's position
how much it is away from left, right, up and down and take min of this position
min(left, right, up down)
this minimum value will be the value at that index.

left = column
right = N - column
up = row
down = N - row

so minimum of (left,right,up,down)
'''

def pattern9(n):
    origi = n
    n = 2*n
    for row in range(1, n):
        for col in range(1, n):
            atEveryIndex = origi - min(min(row, col),min(n-row,n-col)) 
            print(atEveryIndex, end = " ")
        print()

'''
Pattern 10:
1 1 1 1 1 1 1 1 1 
1 2 2 2 2 2 2 2 1 
1 2 3 3 3 3 3 2 1 
1 2 3 4 4 4 3 2 1 
1 2 3 4 5 4 3 2 1 
1 2 3 4 4 4 3 2 1 
1 2 3 3 3 3 3 2 1 
1 2 2 2 2 2 2 2 1 
1 1 1 1 1 1 1 1 1
'''
        
def pattern10(n):
    n = 2*n
    for row in range(1, n):
        for col in range(1, n):
            atEveryIndex = min(min(row, col),min(n-row,n-col)) 
            print(atEveryIndex, end = " ")
        print()


''' 
Pattern 11:

    *
   **
  ***
 ****
*****
'''


def pattern11(n):
    for row in range(0,n+1):
        spaces = n - row
        for space in range(0, spaces):
            print(end = " ")
        for col in range(0, row):
            print("*",end = "")
        print()

'''
pattern 12: 

*****
 ****
  ***
   **
    *
'''

def pattern12(n):
    for row in range(0,n+1):
        for space in range(0, row):
            print(end = " ")
        for col in range(0, n-row):
            print("*",end = "")
        print()
        
'''
Pattern13:
    *
   ***
  *****
 *******
*********
'''

def pattern13(n):
    for row in range(0,n):
        for space in range(0, n-row):
            print(end = "  ")
        cols = row * 2 + 1 
        for col in range(0,cols):
            print("*",end = " ")
        print()

'''
Pattern 14: 
    *********
     *******
      *****
       ***
        *
'''
def pattern14(n):
    for row in range(0,n):
        for space in range(0, row):
            print(end = "  ")
        cols = (n*2) - (row * 2 + 1) 
        for col in range(0,cols):
            print("*",end = " ")
        print()

'''
Pattern 15:
         *
        * *
       * * *
      * * * *
     * * * * *
'''

def pattern15(n):
    for row in range(0,n):
        for space in range(0, n-row):
            print(end =" ")
        for col in range(0, row+1):
            print("*",end = " ")
        print()

'''
Pattern 16:
     * * * * *
      * * * *
       * * *
        * *
         *

'''

def pattern16(n):
    for row in range(0,n):
        for space in range(0, row):
            print(end =" ")
        for col in range(0, n-row):
            print("*",end = " ")
        print()
        
'''
Pattern 17:
     * * * * *
      * * * *
       * * *
        * *
         *
         *
        * *
       * * *
      * * * *
     * * * * *

'''

def pattern17(n):
    for row in range(0,2*n):
        spaces = row+1 if row < n else 2*n - row
        for space in range(0,spaces):
            print(end =" ")
        cols = n - row if row < n else row+1 - n
        for col in range(0,cols):
            print("*",end =" ")
        print()

       
pattern1(n)
print()
pattern2(n)
print()
pattern3(n)
print()
pattern4(n)
print()
pattern5(n)
print()
pattern6(n)
print()
pattern7(n)
print()
pattern8(n)
print()
pattern9(n)
print()
pattern10(n)
print()
pattern11(n)
print()
pattern12(n)
print()      
pattern13(n)
print() 
pattern14(n)
print() 
pattern15(n)
print()
pattern16(n)
print()
pattern17(n)
print()      