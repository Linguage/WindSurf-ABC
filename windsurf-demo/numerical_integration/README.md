# Numerical Integration Module

This module provides various numerical methods for approximating definite integrals.

## Installation

```bash
# Clone the repository
# Install the package in development mode
pip install -e .
```

## Usage

```python
from numerical_integration import integrate, trapezoidal, simpsons, midpoint
import math

# Define a function to integrate
def f(x):
    return math.sin(x)

# Using the general integrate function with different methods
result_trap = integrate(f, 0, math.pi, method='trapezoidal', n=1000)
result_simp = integrate(f, 0, math.pi, method='simpsons', n=1000)
result_mid = integrate(f, 0, math.pi, method='midpoint', n=1000)

print(f"Trapezoidal rule result: {result_trap}")
print(f"Simpson's rule result: {result_simp}")
print(f"Midpoint rule result: {result_mid}")

# Or use the functions directly
result = trapezoidal(f, 0, math.pi, n=1000)
print(f"Direct trapezoidal result: {result}")
```

## Available Methods

1. **Trapezoidal Rule** (`trapezoidal`)
   - Simple and robust
   - Good for smooth functions
   - Error: O(h²)

2. **Simpson's Rule** (`simpsons`)
   - More accurate for smooth functions
   - Requires even number of intervals (n must be even)
   - Error: O(h⁴)

3. **Midpoint Rule** (`midpoint`)
   - Simple to implement
   - Good for certain types of functions
   - Error: O(h²)

## Running Tests

```bash
# Install test dependencies
pip install pytest

# Run tests
pytest tests/
```

## Example: Calculating π

```python
# Calculate π by integrating 4/(1 + x²) from 0 to 1
# The exact value should be π

def f(x):
    return 4 / (1 + x**2)

pi_approx = integrate(f, 0, 1, method='simpsons', n=10000)
print(f"Approximation of π: {pi_approx}")
print(f"Actual value of π: {math.pi}")
print(f"Error: {abs(pi_approx - math.pi)}")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
