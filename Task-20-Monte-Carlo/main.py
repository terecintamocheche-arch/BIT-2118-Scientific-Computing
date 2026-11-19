
import numpy as np
import matplotlib.pyplot as plt

# Input value
number_of_points = 10000

# Generate random points
x = np.random.uniform(-1, 1, number_of_points)
y = np.random.uniform(-1, 1, number_of_points)

# Check which points fall inside the circle
inside_circle = x**2 + y**2 <= 1

# Estimate pi
inside_count = np.sum(inside_circle)
pi_estimate = 4 * inside_count / number_of_points

print("Total random points:", number_of_points)
print("Points inside circle:", inside_count)
print("Estimated value of pi:", pi_estimate)
print("Actual value of pi:", np.pi)

# Plot the points
plt.scatter(x[inside_circle], y[inside_circle], s=2, label="Inside circle")
plt.scatter(x[~inside_circle], y[~inside_circle], s=2, label="Outside circle")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Monte Carlo Estimation of Pi")
plt.axis("equal")
plt.legend()
plt.show()
