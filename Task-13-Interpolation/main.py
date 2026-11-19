
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# Recorded hourly temperatures
hours = np.array([8, 9, 10, 11, 12])
temperatures = np.array([20, 22, 25, 27, 30])

# Create interpolation functions
linear = interp1d(hours, temperatures)
cubic = CubicSpline(hours, temperatures)

# Estimate temperature at 10:30
time = 10.5
linear_result = linear(time)
cubic_result = cubic(time)

print("Linear interpolation:", linear_result)
print("Cubic interpolation:", cubic_result)

# Plot results
x = np.linspace(8, 12, 100)
plt.scatter(hours, temperatures, label="Recorded temperatures")
plt.plot(x, linear(x), label="Linear")
plt.plot(x, cubic(x), label="Cubic")
plt.xlabel("Hour")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Interpolation")
plt.legend()
plt.grid()
plt.show()
