"""
Solution for Exercise 1: Basic Combinatorics
"""


def factorial(n: int) -> int:
    """Calculate n!"""
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def binomial_coefficient(n: int, k: int) -> int:
    """Calculate C(n, k)"""
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    # Use symmetry: C(n, k) = C(n, n-k)
    k = min(k, n - k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result
