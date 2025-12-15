"""
Exercise 4: Exact Distribution

Implement exact_distribution function.
"""

# Import position_probability_given_cables from Lecture 3
# Try importing from exercise first (your implementation), fall back to solution
try:
    from lecture_03_position_probability.exercise import position_probability_given_cables
except (ImportError, NotImplementedError):
    from lecture_03_position_probability.solution import position_probability_given_cables


def exact_distribution(number_of_players: int, available_numbers: int, number_instances: int) -> list[list[float]]:
    """
    Calculate exact probability distribution using combinatorics.
    
    Returns the same format as sample_distribution:
    list[list[float]] where result[i][j] is the probability that 
    number (i+1) appears at position j for player 0.
    
    Args:
        number_of_players: Number of players (P)
        available_numbers: Number of different numbers (N)
        number_instances: Number of instances of each number (M)
        
    Returns:
        Distribution matrix: result[i][j] = P(number i+1 at position j)
        
    Example:
        # 4 players, 4 numbers, 4 instances each
        dist = exact_distribution(4, 4, 4)
        # dist[0][0] should be approximately 0.728
    """
    # TODO: Implement this function
    raise NotImplementedError("exact_distribution not yet implemented")
