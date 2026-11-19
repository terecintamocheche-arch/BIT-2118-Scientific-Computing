
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Input values
initial_population = 100
growth_rate = 0.2
start_time = 0
end_time = 10

# Differential equation
def population_growth(time, population):
    return growth_rate * population

# Solve using SciPy
solution = solve_ivp(
    population_growth,
    [start_time, end_time],
    [initial_population],
    t_eval=np.linspace(start_time, end_time, 100)
)

print("Initial population:", initial_population)
print("Population after 10 years:", solution.y[0][-1])

# Plot results
plt.plot(solution.t, solution.y[0])
plt.xlabel("Time (years)")
plt.ylabel("Population")
plt.title("Population Growth Using SciPy")
plt.grid()
plt.show()

