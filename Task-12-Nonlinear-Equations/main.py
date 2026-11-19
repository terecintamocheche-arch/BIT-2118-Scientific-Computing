
import numpy as np
from scipy.optimize import root

# Define the equations
def equations(values):
    x, y = values
    return [
        x**2 + y**2 - 4,
        y - x**2 + 1
    ]

# Initial guess
initial_guess = [1, 1]

# Solve equations
result = root(equations, initial_guess)

print("Solution:", result.x)
print("Converged:", result.success)
print("Equation results:", equations(result.x))
