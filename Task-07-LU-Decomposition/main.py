
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Coefficient matrix
A = np.array([
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 3]
])

# Different measurement values
measurements = [
    np.array([15, 10, 10]),
    np.array([20, 15, 12])
]

# Perform LU factorization
lu, piv = lu_factor(A)

# Solve each system
for i, b in enumerate(measurements, start=1):
    solution = lu_solve((lu, piv), b)
    print(f"Measurement {i}:", solution)
    print("Verification:", A @ solution)
