"""
Tests for the numerical integration module.
"""

import math
import pytest
from numerical_integration import trapezoidal, simpsons, midpoint, integrate


def test_trapezoidal_simple():
    """Test trapezoidal rule with a simple linear function."""
    def f(x):
        return 2 * x  # Integral from 0 to 1 should be 1.0
    
    result = trapezoidal(f, 0, 1, n=1000)
    assert math.isclose(result, 1.0, rel_tol=1e-5)


def test_simpsons_quadratic():
    """Test Simpson's rule with a quadratic function."""
    def f(x):
        return x ** 2  # Integral from 0 to 1 should be 1/3
    
    result = simpsons(f, 0, 1, n=1000)
    assert math.isclose(result, 1/3, rel_tol=1e-6)

def test_midpoint_sine():
    """Test midpoint rule with sine function."""
    def f(x):
        return math.sin(x)  # Integral from 0 to π should be 2.0
    
    result = midpoint(f, 0, math.pi, n=10000)
    assert math.isclose(result, 2.0, rel_tol=1e-5)

def test_integrate_function():
    """Test the general integrate function with different methods."""
    def f(x):
        return 3 * x ** 2  # Integral from 0 to 1 should be 1.0
    
    methods = ['trapezoidal', 'simpsons', 'midpoint']
    for method in methods:
        result = integrate(f, 0, 1, method=method, n=1000)
        assert math.isclose(result, 1.0, rel_tol=1e-5), f"Failed with method: {method}"

def test_invalid_method():
    """Test that invalid method raises ValueError."""
    with pytest.raises(ValueError):
        integrate(lambda x: x, 0, 1, method='invalid_method')

def test_invalid_n():
    """Test that invalid n raises ValueError."""
    with pytest.raises(ValueError):
        trapezoidal(lambda x: x, 0, 1, n=0)
    with pytest.raises(ValueError):
        simpsons(lambda x: x, 0, 1, n=1)  # n must be even for Simpson's rule
