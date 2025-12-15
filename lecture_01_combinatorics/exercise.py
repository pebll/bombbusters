"""
Exercise 1: Basic Combinatorics

Implement factorial and binomial_coefficient functions.
"""


def factorial(n: int) -> int:
    """
    Calculate n! = n × (n-1) × ... × 2 × 1
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Examples:
        factorial(0) = 1
        factorial(3) = 6
        factorial(5) = 120
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return n * factorial(n-1)


def binomial_coefficient(n: int, k: int) -> int:
    """
    Calculate C(n, k) = n! / (k! × (n-k)!)
    
    This is the number of ways to choose k items from n items.
    
    Args:
        n: Total number of items
        k: Number of items to choose
        
    Returns:
        Number of ways to choose k items from n items
        
    Examples:
        binomial_coefficient(5, 2) = 10
        binomial_coefficient(10, 0) = 1
        binomial_coefficient(10, 10) = 1
        binomial_coefficient(5, 7) = 0 (k > n)
    """
    # Efficient calculations: it's bullshit right?
    # C(10, 9) = 10! / (9! * 1!) = 20 computations
    # C(10, 1) = 10! / (1! * (10 -1!)) = 20 computations
    if k > n or n < 0 or k < 0:
        return 0
    return factorial(n) / (factorial(k) * factorial(n-k))
