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