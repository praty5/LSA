import numpy as np

def jacobi(matrix):
    tolerance=1e-6 
    n = len(matrix)
    identity = np.identity(n) # create an identity matrix
    x = np.zeros((n,n))  # create a zero matrix

    # Perform the Jacobi iteration
    for k in range(1000):
        x_old = x.copy()  # create copy of x to compare with the new x

        # Solve for each column of the identity matrix and find the inverse matrix
        for i in range(n):
            x[i] = (identity[i] - np.dot(matrix[i], x_old) + matrix[i, i] * x_old[i]) / matrix[i, i]
       
        # check if the difference between the old and new x is less than the tolerance
        if np.allclose(x,x_old, atol=tolerance):
            print("Number of iterations:", k)
            return x

# Read the input matrix from a text file
with open("input.txt", "r") as file:
    n = int(file.readline())
    matrix = []
    for _ in range(n):
        row = [float(x) for x in file.readline().split()]
        matrix.append(row)

# Convert the input matrix to a numpy array and call the inverse function
A = np.array(matrix)
inverse_matrix = jacobi(A)

print("Inverse of the matrix:")
print(inverse_matrix)

