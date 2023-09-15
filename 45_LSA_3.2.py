import numpy as np
import os
#Taking input for size of the matrices
print("  A  *  X  =  B  ")
row1=int(input("Enter the number of rows of matrix A: "))
col1=int(input("Enter the number of columns of matrix A: "))
print()
row2=int(input("Enter the number of rows of matrix B: "))
col2=int(input("Enter the number of columns of matrix B: "))
print()
if not col1==row2:
    print("Invalid input - Cannot multiply the matrix of the given dimensions.")
    exit()

m1=[] #first matrix
m2=[] #second matrix
result=[[0 for j in range(col2)] for i in range(row1)] #initializing the result matrix

os.system("cls" if os.name == "nt" else "clear")

for i in range(row1):
    m1.append([]) #adding a new row
    for j in range(col1):
        m1[i].append(int(input(f"Enter the [{i+1} {j+1}] element of matrix A: ")))
#calculate the inverse of m1 using numpy library
invm=np.linalg.inv(m1)

os.system("cls" if os.name == "nt" else "clear")

for i in range(row2):
    m2.append([]) # adding a new row
    for j in range(col2):
        m2[i].append(int(input(f"Enter the [{i+1} {j+1}] element of matrix B: ")))

#multiplying the inverse of m1 with m2
for i in range(row1):
    for j in range(col2):
        for k in range(col1):
            result[i][j]+=invm[i][k]*m2[k][j]

print("\nThe matrix X is: ")
for i in range(row1):
    for j in range(col2):
        print(result[i][j],end=" ")
    print()
print()
