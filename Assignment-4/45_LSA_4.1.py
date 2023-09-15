import numpy as np

# inverse using LU decomposition
def inverse(matrix):
    L, U = lu_decomposition(matrix) # create L and U matrices
    n = len(matrix)
    identity_matrix = np.identity(n) # create an identity matrix
    inverse_matrix = np.zeros((n, n)) # create a zero matrix
    # Solve for each column of the identity matrix and find the inverse matrix
    for i in range(n):
        # Solve LY = I
        y = np.linalg.solve(L, identity_matrix[:, i]) # solve for y
        # Solve UX = y
        x = np.linalg.solve(U, y) # solve for x
        inverse_matrix[:, i] = x # add x to the inverse matrix

    return inverse_matrix

# LU decomposition
def lu_decomposition(matrix):
    n = len(matrix)
    L = np.identity(n) # create an identity matrix
    U = np.copy(matrix) # create a copy of the input matrix
    # Perform the LU decomposition
    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]
    return L, U

# Read the input matrix from a text file
with open('input.txt', 'r') as file:
    n = int(file.readline())
    input_matrix = []
    for _ in range(n):
        row = list(map(float, file.readline().split()))
        input_matrix.append(row)

# convert the input matrix to a numpy array and call the inverse function
input_matrix = np.array(input_matrix) 
inverse_matrix = inverse(input_matrix)

print("Inverse of the matrix:")
print(inverse_matrix)
