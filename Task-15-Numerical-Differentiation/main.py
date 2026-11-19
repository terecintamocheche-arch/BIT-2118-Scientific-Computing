
import numpy as np
import matplotlib.pyplot as plt

# Input values
time = np.array([0, 1, 2, 3, 4, 5])
position = np.array([0, 2, 8, 18, 32, 50])

# Numerical differentiation
velocity = np.gradient(position, time)

print("Time:", time)
print("Position:", position)
print("Estimated velocity:", velocity)

# Plot position and velocity
plt.plot(time, position, marker="o", label="Position")
plt.xlabel("Time (seconds)")
plt.ylabel("Position (metres)")
plt.title("Position over Time")
plt.legend()
plt.grid()
plt.show()

plt.plot(time, velocity, marker="o", label="Velocity")
plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity over Time")
plt.legend()
plt.grid()
plt.show()
