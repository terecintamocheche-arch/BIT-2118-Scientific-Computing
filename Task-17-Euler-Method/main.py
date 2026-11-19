
import numpy as np
import matplotlib.pyplot as plt

# Input values
initial_temperature = 90
room_temperature = 25
cooling_rate = 0.1
time_step = 1
total_time = 10

# Create time values
time = np.arange(0, total_time + time_step, time_step)

# Store temperature values
temperature = [initial_temperature]

# Euler's method
for i in range(len(time) - 1):
    current_temperature = temperature[-1]

    rate_of_change = -cooling_rate * (
        current_temperature - room_temperature
    )

    new_temperature = current_temperature + time_step * rate_of_change
    temperature.append(new_temperature)

print("Initial temperature:", initial_temperature)
print("Temperature after 10 minutes:", temperature[-1])

# Plot results
plt.plot(time, temperature, marker="o")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Cooling of Hot Water Using Euler's Method")
plt.grid()
plt.show()
