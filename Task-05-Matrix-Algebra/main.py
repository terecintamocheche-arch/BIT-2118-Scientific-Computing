
import numpy as np

# Original square coordinates
points = np.array([
    [0, 0],
    [2, 0],
    [2, 2],
    [0, 2]
])

# Transformation matrix for rotation
rotation = np.array([
    [0, -1],
    [1,  0]
])

# Transformation matrix for scaling
scaling = np.array([
    [2, 0],
    [0, 2]
])

# Apply transformations
rotated_points = points @ rotation.T
transformed_points = rotated_points @ scaling.T

print("Original points:")
print(points)

print("\nRotated points:")
print(rotated_points)

print("\nRotated and scaled points:")
print(transformed_points)
