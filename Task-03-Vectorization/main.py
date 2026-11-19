
import numpy as np
import time

# Simulate network latency measurements
latency = np.random.randint(10, 101, 1000000)

# Calculate using a Python loop
start = time.time()

total = 0
for value in latency:
    total += value

loop_average = total / len(latency)
loop_time = time.time() - start

# Calculate using NumPy vectorization
start = time.time()

numpy_average = np.mean(latency)
numpy_time = time.time() - start

print("Python loop average:", loop_average)
print("NumPy average:", numpy_average)
print("Python loop time:", loop_time)
print("NumPy time:", numpy_time)
