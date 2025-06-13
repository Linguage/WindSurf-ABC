"""
Numerical Integration Module

This module provides various numerical methods for approximating definite integrals.
It includes implementations of common numerical integration techniques such as
the Trapezoidal rule, Simpson's rule, and Midpoint rule.
"""

from .integrators import (
    trapezoidal,
    simpsons,
    midpoint,
    integrate  # General purpose integration function
)

__all__ = ['trapezoidal', 'simpsons', 'midpoint', 'integrate']
