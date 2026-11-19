
import numpy as np
from scipy.optimize import root_scalar

# Heat balance equation
def f(T):
    return T - 25 - 10 * np.exp(-T / 20)

# Bisection method
bisection = root_scalar(f, bracket=[25, 40], method="bisect")

# Fixed-point iteration
T = 30
for i in range(100):
    T = 25 + 10 * np.exp(-T / 20)

print("Bisection root:", bisection.root)
print("Fixed-point result:", T)
print("Bisection converged:", bisection.converged)
