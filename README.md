# BIT-2118-Scientific-Computing
# Task 2: NumPy Arrays and Numerical Computation

## 1. Introduction
This task uses NumPy to analyse hourly temperature readings collected from a weather station.

## 2. Input Values
The program uses 24 temperature readings measured in degrees Celsius.

## 3. Mathematical Operations
- `np.mean()` calculates the average temperature.
- `np.min()` finds the minimum temperature.
- `np.max()` finds the maximum temperature.
- Celsius is converted to Fahrenheit using the formula: F = (C × 1.8) + 32.

## 4. Original Output
- Average temperature: 25.5°C
- Minimum temperature: 21°C
- Maximum temperature: 31°C

## 5. Output Interpretation
The average temperature throughout the day was 25.5°C. The lowest recorded temperature was 21°C, while the highest was 31°C. The Fahrenheit conversion provides the same readings in a different temperature scale.

## 6. Real-World Application
This program can help weather stations analyse daily temperature patterns and provide useful information for weather monitoring and agricultural planning.

## 7. Changing an Input Parameter
I changed one temperature reading from 31°C to 35°C. As a result, the average temperature increased from 25.5°C to approximately 25.67°C, while the maximum temperature increased from 31°C to 35°C. This demonstrates how changing an input affects the calculated results.

# Task 3: Mathematical Functions and Vectorization

## Input Values
The program generates 1,000,000 random network latency measurements between 10 and 100 milliseconds.

## Mathematical Operation
The program calculates the average latency using a Python loop and NumPy's `mean()` function. It also measures the execution time of both methods.

## Output Interpretation
Both methods calculate the average latency. NumPy vectorization generally performs the calculation faster because it processes the array efficiently.

## Changing an Input
The number of measurements can be changed from 1,000,000 to 500,000. This reduces the amount of data processed and generally reduces execution time.

## Real-World Application
This method can be used to analyse network performance and monitor internet response times.

# Task 4: Floating-Point Arithmetic and Numerical Errors

## Input Values
The program uses decimal values 0.1 and 0.2 and an approximation of the square root of 2 (1.414).

## Mathematical Operations
- Addition of floating-point numbers.
- Calculation of the square root using NumPy.
- Absolute error and relative error calculations.

## Output Interpretation
The addition of 0.1 and 0.2 may produce a value slightly different from 0.3 because computers store decimal numbers in binary floating-point format. NumPy's `isclose()` checks whether the values are sufficiently close.

The absolute and relative errors show the difference between the exact square root and its approximation.

## Changing an Input
Change the approximation from 1.414 to 1.4. The absolute and relative errors will increase because the approximation becomes less accurate.

## Real-World Application
Floating-point accuracy is important in scientific simulations, engineering calculations and financial computations.

# Task 5: Matrix Algebra and Matrix Operations

## Input Values
The program uses four coordinate points representing a square and two transformation matrices.

## Mathematical Operations
- Matrix multiplication.
- Rotation of coordinates by 90 degrees.
- Scaling coordinates by a factor of 2.

## Output Interpretation
The original square is rotated and enlarged. The resulting coordinates show the new positions of the points after both transformations.

## Changing an Input
Change the scaling matrix values from 2 to 3. The square becomes larger because its coordinates are multiplied by a greater scaling factor.

## Modified Real-World Application
The program can be used in a computer graphics system to rotate and resize objects displayed on a screen.

# Task 6: Solution of Systems of Linear Equations

## Input Values
The program uses the coefficient matrix A = [[4, 2], [8, 12]] and the result vector B = [20, 72].

## Mathematical Operation
NumPy's `np.linalg.solve()` solves two simultaneous linear equations to find the unknown values.

## Output Interpretation
The solution is 3 units of Server Type A and 4 units of Server Type B. The verification confirms that these values satisfy both equations.

## Changing an Input
Change the first result value from 20 to 24. The solution changes because the system now has a different requirement.

## Modified Real-World Application
This method can be used to allocate computing resources based on different server capacities and resource requirements.

# Task 7: Gaussian Elimination and LU Decomposition

## Input Values
The program uses a 3 × 3 coefficient matrix and two different measurement vectors.

## Mathematical Operation
LU decomposition separates a matrix into lower and upper triangular factors. SciPy's `lu_factor()` performs the factorization, while `lu_solve()` solves the systems.

## Output Interpretation
The program produces solutions for two measurement systems using the same coefficient matrix. Verification confirms that the solutions satisfy the original equations.

## Changing an Input
Change the first value of the first measurement vector from 15 to 20. This changes the calculated solution.

## Modified Real-World Application
This method can be used in engineering simulations where several measurement sets need to be analysed using the same system of equations.

# Task 8: Iterative Methods for Linear Systems

## Input Values
The program uses a 3 × 3 coefficient matrix, a temperature vector and initial estimates of zero.

## Mathematical Operation
The Jacobi and Gauss-Seidel iterative methods repeatedly update estimated values until they approach a solution.

## Output Interpretation
Both methods estimate the temperature values. The graph shows how the error changes with each iteration. A decreasing error indicates convergence towards the solution.

## Changing an Input
Increase the number of iterations from 20 to 30. This gives the methods more opportunities to approach the solution.

## Modified Real-World Application
These methods can be used to estimate temperature distribution in buildings or other systems involving heat transfer.

# Task 9: Eigenvalues and Eigenvectors

## Input Values
The program uses a 4 × 4 adjacency matrix representing connections between four computers.

## Mathematical Operation
NumPy's `np.linalg.eig()` calculates the eigenvalues and eigenvectors of the matrix. The dominant eigenvector is used to calculate normalized centrality scores.

## Output Interpretation
The centrality scores indicate the relative importance of each computer in the network. A higher score means the computer is more central based on its connections.

## Changing an Input
Add a connection between Computer 1 and Computer 4 by changing the corresponding matrix entries from 0 to 1. The network structure and centrality scores will change.

## Modified Real-World Application
This method can be used to identify important devices in computer networks or influential pages in a web-link network.

# Task 10: Root Finding – Bisection and Fixed-Point Methods

## Input Values
The program uses a heat-balance equation with a constant temperature of 25 and a heat factor of 10.

## Mathematical Operation
The Bisection method repeatedly divides an interval to find a root. Fixed-point iteration repeatedly substitutes an estimated value into the equation.

## Output Interpretation
Both methods estimate the temperature at which the heat-balance equation equals zero. Similar results indicate that both methods have approached the same root.

## Changing an Input
Change the heat factor from 10 to 15. This changes the equation and produces a different equilibrium temperature.

## Modified Real-World Application
Root-finding methods can be used to estimate equilibrium temperatures in heating and cooling systems.

# Task 11: Newton-Raphson and Secant Methods

## Input Values
The program uses an initial investment of 10,000 and future cash flows of 3,000, 3,500, 4,000 and 2,500.

## Mathematical Operation
The Newton-Raphson and Secant methods estimate the root of the Net Present Value equation. The root represents the Internal Rate of Return (IRR).

## Output Interpretation
The calculated IRR represents the discount rate at which the investment's net present value becomes zero. Both methods should produce similar results.

## Changing an Input
Change the final cash flow from 2,500 to 3,000. This increases the expected return and changes the calculated IRR.

## Modified Real-World Application
These methods can help investors evaluate the profitability of projects and business investments.

# Task 12: Polynomial and Nonlinear Equation Solving

## Input Values
The program uses a circle equation, x² + y² = 4, and a parabola equation, y = x² - 1.

## Mathematical Operation
SciPy's `root()` function solves the system of nonlinear equations using an initial estimate of x = 1 and y = 1.

## Output Interpretation
The output gives the coordinates where the circle and parabola intersect. A successful convergence indicates that the solver found a solution.

## Changing an Input
Change the initial guess from [1, 1] to [0.5, 1]. This may lead the solver to a different intersection point.

## Modified Real-World Application
Nonlinear equation solving can be used in engineering to calculate the intersection of curves and model relationships between variables.