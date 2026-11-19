
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Input data
users = np.array([50, 100, 150, 200, 250, 300])
response_time = np.array([0.8, 1.1, 1.5, 2.2, 3.0, 4.1])

# Quadratic model
def model(x, a, b, c):
    return a*x**2 + b*x + c

# Fit the curve
parameters, covariance = curve_fit(model, users, response_time)

# Predictions
predictions = model(users, *parameters)
rmse = np.sqrt(np.mean((response_time - predictions)**2))

# Predict response time for 400 users
new_prediction = model(400, *parameters)

print("Model parameters:", parameters)
print("RMSE:", rmse)
print("Predicted response time for 400 users:", new_prediction)

# Plot
plt.scatter(users, response_time, label="Actual data")
x = np.linspace(50, 400, 100)
plt.plot(x, model(x, *parameters), label="Fitted curve")
plt.xlabel("Number of users")
plt.ylabel("Response time (seconds)")
plt.title("Server Response Time Curve Fitting")
plt.legend()
plt.grid()
plt.show()

