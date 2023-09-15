import os
#Taking input for size of the matrices
size1=int(input("Enter the size of first square matrix: "))
print()
size2=int(input("Enter the size of second square matrix: "))
print()
if not size1==size2:
    print("Invalid input - Cannot multiply the matrix of the given dimensions.")
    exit()

m1=[] #first matrix
m2=[] #second matrix
result=[[0 for j in range(size1)] for i in range(size1)] #initializing the result matrix

os.system("cls" if os.name == "nt" else "clear")

for i in range(size1):
    m1.append([]) # adding a new row
    for j in range(size1):
        m1[i].append(int(input(f"Enter the [{i+1} {j+1}] element of first matrix: ")))
print()

os.system("cls" if os.name == "nt" else "clear")

for i in range(size1):
    m2.append([]) # adding a new row
    for j in range(size1):
        m2[i].append(int(input(f"Enter the [{i+1} {j+1}] element of second matrix: ")))

os.system("cls" if os.name == "nt" else "clear")

for i in range(size1):
    for j in range(size1):
        for k in range(size1):
            result[i][j]+=m1[i][k]*m2[k][j]

#print(result)
print("\nThe resultant matrix is: ")
for i in range(size1):
    for j in range(size1):
        print(result[i][j],end=" ")
    print()
print()