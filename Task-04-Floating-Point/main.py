
import numpy as np

# Floating-point arithmetic
a = 0.1
b = 0.2
result = a + b

print("0.1 + 0.2 =", result)
print("Is the result close to 0.3?", np.isclose(result, 0.3))

# Calculate square root of 2
exact_value = np.sqrt(2)
approximation = 1.414

absolute_error = abs(exact_value - approximation)
relative_error = absolute_error / exact_value

print("Square root of 2:", exact_value)
print("Approximation:", approximation)
print("Absolute error:", absolute_error)
print("Relative error:", relative_error)
