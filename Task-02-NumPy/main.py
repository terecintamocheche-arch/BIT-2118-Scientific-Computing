import numpy as np

# Hourly temperature readings in Celsius
temperatures = np.array([
    22, 23, 24, 25, 26, 27,
    28, 29, 30, 31, 30, 29,
    28, 27, 26, 25, 24, 23,
    22, 21, 22, 23, 24, 23
])

# Calculate temperature statistics
average = np.mean(temperatures)
minimum = np.min(temperatures)
maximum = np.max(temperatures)

# Convert Celsius to Fahrenheit
fahrenheit = (temperatures * 1.8) + 32

print("Average temperature:", average, "°C")
print("Minimum temperature:", minimum, "°C")
print("Maximum temperature:", maximum, "°C")
print("Temperatures in Fahrenheit:", fahrenheit)