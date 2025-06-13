"""
Numerical integration methods implementation.

This module contains various numerical methods for approximating definite integrals.
"""

import numpy as np
from typing import Callable, Tuple, Optional


def trapezoidal(f: Callable[[float], float], a: float, b: float, n: int = 1000) -> float:
    """
    Approximate the definite integral of f from a to b using the Trapezoidal rule.
    
    Args:
        f: Function to integrate
        a: Lower bound of integration
        b: Upper bound of integration
        n: Number of subintervals (default: 1000)
        
    Returns:
        Approximate value of the integral
    """
    if n <= 0:
        raise ValueError("Number of subintervals (n) must be positive")
        
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        result += f(a + i * h)
        
    return result * h


def simpsons(f: Callable[[float], float], a: float, b: float, n: int = 1000) -> float:
    """
    Approximate the definite integral of f from a to b using Simpson's rule.
    
    Args:
        f: Function to integrate
        a: Lower bound of integration
        b: Upper bound of integration
        n: Number of subintervals (must be even, default: 1000)
        
    Returns:
        Approximate value of the integral
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's rule")
        
    h = (b - a) / n
    result = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * f(x)
        else:
            result += 4 * f(x)
            
    return result * h / 3


def midpoint(f: Callable[[float], float], a: float, b: float, n: int = 1000) -> float:
    """
    Approximate the definite integral of f from a to b using the Midpoint rule.
    
    Args:
        f: Function to integrate
        a: Lower bound of integration
        b: Upper bound of integration
        n: Number of subintervals (default: 1000)
        
    Returns:
        Approximate value of the integral
    """
    if n <= 0:
        raise ValueError("Number of subintervals (n) must be positive")
        
    h = (b - a) / n
    result = 0.0
    
    for i in range(n):
        x_mid = a + (i + 0.5) * h
        result += f(x_mid)
        
    return result * h


def integrate(f: Callable[[float], float], a: float, b: float, 
              method: str = 'trapezoidal', n: int = 1000) -> float:
    """
    General purpose numerical integration function.
    
    Args:
        f: Function to integrate
        a: Lower bound of integration
        b: Upper bound of integration
        method: Integration method ('trapezoidal', 'simpsons', or 'midpoint')
        n: Number of subintervals
        
    Returns:
        Approximate value of the integral
        
    Raises:
        ValueError: If an invalid method is specified
    """
    methods = {
        'trapezoidal': trapezoidal,
        'simpsons': simpsons,
        'midpoint': midpoint,
    }
    
    if method not in methods:
        raise ValueError(f"Unknown method: {method}. Available methods: {list(methods.keys())}")
    
    return methods[method](f, a, b, n)
