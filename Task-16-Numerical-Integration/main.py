
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

# Input values
time = np.array([0, 1, 2, 3, 4, 5])
velocity = np.array([0, 5, 10, 15, 20, 25])

# Numerical integration
distance = trapezoid(velocity, time)

print("Time:", time)
print("Velocity:", velocity)
print("Total distance travelled:", distance, "metres")

# Plot velocity against time
plt.plot(time, velocity, marker="o")
plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity Against Time")
plt.grid()
plt.show()

