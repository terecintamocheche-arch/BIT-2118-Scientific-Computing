
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Profit function
def profit(quantity):
    revenue = 100 * quantity
    cost = 0.5 * quantity**2 + 20 * quantity + 500
    return revenue - cost

# Minimize negative profit to find maximum profit
result = minimize_scalar(
    lambda quantity: -profit(quantity),
    bounds=(0, 100),
    method="bounded"
)

best_quantity = result.x
maximum_profit = profit(best_quantity)

print("Optimal production quantity:", round(best_quantity, 2))
print("Maximum profit:", round(maximum_profit, 2))

# Plot profit
quantities = np.linspace(0, 100, 100)
profits = profit(quantities)

plt.plot(quantities, profits)
plt.scatter(best_quantity, maximum_profit, label="Maximum profit")
plt.xlabel("Production quantity")
plt.ylabel("Profit")
plt.title("Profit Optimization")
plt.legend()
plt.grid()
plt.show()
