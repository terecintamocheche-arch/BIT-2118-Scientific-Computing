
import numpy as np
from scipy.optimize import newton

# Investment cash flows
cash_flows = [-10000, 3000, 3500, 4000, 2500]

# Net present value equation
def npv(rate):
    return sum(
        cash_flows[t] / (1 + rate) ** t
        for t in range(len(cash_flows))
    )

# Newton-Raphson method
newton_result = newton(npv, 0.1)

# Secant method
secant_result = newton(npv, 0.1, x1=0.2)

print("Newton-Raphson IRR:", newton_result)
print("Secant IRR:", secant_result)
print("Newton-Raphson percentage:", newton_result * 100, "%")
