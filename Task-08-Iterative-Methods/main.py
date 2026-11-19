
import numpy as np
import matplotlib.pyplot as plt

# Coefficient matrix and temperature values
A = np.array([
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 4]
], dtype=float)

b = np.array([100, 100, 100], dtype=float)

# Initial temperature estimates
x = np.zeros(3)
jacobi = x.copy()
gauss_seidel = x.copy()

# Store errors for graph
jacobi_errors = []
gs_errors = []

# Jacobi and Gauss-Seidel iterations
for i in range(20):
    old = jacobi.copy()
    for j in range(3):
        jacobi[j] = (b[j] - (A[j] @ old - A[j, j] * old[j])) / A[j, j]

    for j in range(3):
        gauss_seidel[j] = (
            b[j] - (A[j] @ gauss_seidel - A[j, j] * gauss_seidel[j])
        ) / A[j, j]

    jacobi_errors.append(np.linalg.norm(A @ jacobi - b))
    gs_errors.append(np.linalg.norm(A @ gauss_seidel - b))

print("Jacobi solution:", jacobi)
print("Gauss-Seidel solution:", gauss_seidel)

plt.plot(jacobi_errors, label="Jacobi")
plt.plot(gs_errors, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Error")
plt.title("Convergence of Iterative Methods")
plt.legend()
plt.grid()
plt.show()

