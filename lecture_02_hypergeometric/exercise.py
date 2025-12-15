"""
Exercise 2: Hypergeometric Distribution

Implement hypergeometric_probability function.
"""

# Import binomial_coefficient from Lecture 1
# Try importing from exercise first (your implementation), fall back to solution
try:
    from lecture_01_combinatorics.exercise import binomial_coefficient
except (ImportError, NotImplementedError):
    from lecture_01_combinatorics.solution import binomial_coefficient


def hypergeometric_probability(N: int, K: int, n: int, k: int) -> float:
    """
    Calculate hypergeometric probability: P(k successes in n draws without replacement)
    
    Formula: P(k successes) = C(K, k) × C(N-K, n-k) / C(N, n)
    
    Args:
        N: Total population size
        K: Number of successes in population
        n: Sample size (number of items drawn)
        k: Number of successes in sample
        
    Returns:
        Probability of getting exactly k successes (between 0.0 and 1.0)
        
    Examples:
        # Drawing 2 red balls from 5 red + 5 blue when drawing 3 total
        hypergeometric_probability(10, 5, 3, 2) ≈ 0.4167
    """

    if N < 0 or n < 0 or k < 0 or K < 0 or n > N or k > K or K > N:
        return 0
    return binomial_coefficient(K, k) * binomial_coefficient(N-K, n-k) / binomial_coefficient(N, n)
