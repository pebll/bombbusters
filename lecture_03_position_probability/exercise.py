"""
Exercise 3: Position Probability

Implement position_probability_given_cables function.
"""

# Import hypergeometric_probability from Lecture 2
# Try importing from exercise first (your implementation), fall back to solution
try:
    from lecture_02_hypergeometric.exercise import hypergeometric_probability
except (ImportError, NotImplementedError):
    from lecture_02_hypergeometric.solution import hypergeometric_probability


def position_probability_given_cables(M: int, T: int, c: int, j: int, 
                                      smaller_numbers_count: int) -> float:
    """
    Calculate P(number i at position j | player has c cables)
    
    After sorting, if a player has:
    - s cables of numbers < i
    - k cables of number i
    - (c - s - k) cables of numbers > i
    
    Then number i occupies positions s through s+k-1.
    
    Args:
        M: Number of instances of number i in the deck
        T: Total number of cables
        c: Number of cables the player receives
        j: Position index (0-indexed)
        smaller_numbers_count: Total number of cables with numbers < i
        
    Returns:
        Probability that number i appears at position j (between 0.0 and 1.0)
        
    Example:
        # P(number 1 at position 0) for player with 4 cables
        position_probability_given_cables(M=4, T=16, c=4, j=0, smaller_numbers_count=0)
        # Should be approximately 0.728
    """
    # TODO: Implement this function
    raise NotImplementedError("position_probability_given_cables not yet implemented")
