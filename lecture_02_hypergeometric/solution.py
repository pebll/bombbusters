"""
Solution for Exercise 2: Hypergeometric Distribution
"""

from lecture_01_combinatorics.solution import binomial_coefficient


def hypergeometric_probability(N: int, K: int, n: int, k: int) -> float:
    """Calculate hypergeometric probability"""
    # Check for invalid inputs
    if k < 0 or k > n or k > K or (n - k) > (N - K):
        return 0.0
    
    numerator = binomial_coefficient(K, k) * binomial_coefficient(N - K, n - k)
    denominator = binomial_coefficient(N, n)
    
    if denominator == 0:
        return 0.0
    
    return numerator / denominator
