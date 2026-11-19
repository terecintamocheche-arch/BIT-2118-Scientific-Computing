
import numpy as np

# Coefficient matrix
A = np.array([
    [4, 2],
    [8, 12]
])

# Results
B = np.array([20, 72])

# Solve the equations
solution = np.linalg.solve(A, B)

print("Server allocation:")
print("Server Type A:", solution[0])
print("Server Type B:", solution[1])

# Verify the solution
print("Verification:", np.dot(A, solution))
