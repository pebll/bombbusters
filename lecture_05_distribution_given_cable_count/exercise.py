"""
Exercise 5: Distribution Given Cable Count

Implement exact_distribution_given_cables function.
"""

# Import position_probability_given_cables from Lecture 3
# Try importing from exercise first (your implementation), fall back to solution
try:
    from lecture_03_position_probability.exercise import position_probability_given_cables
except (ImportError, NotImplementedError):
    from lecture_03_position_probability.solution import position_probability_given_cables


def exact_distribution_given_cables(P: int, N: int, M: int, c: int) -> list[list[float]]:
    """
    Calculate exact probability distribution given that a player has exactly c cables.
    
    Returns the same format as sample_distribution:
    list[list[float]] where result[i][j] is the probability that 
    number (i+1) appears at position j for player 0, given that player 0 has exactly c cables.
    
    Args:
        number_of_players: Number of players (P)
        available_numbers: Number of different numbers (N)
        number_instances: Number of instances of each number (M)
        cables: Exact number of cables the player has (c)
        
    Returns:
        Distribution matrix: result[i][j] = P(number i+1 at position j | player has c cables)
        
    Example:
        # 4 players, 4 numbers, 4 instances each, player has 4 cables
        dist = exact_distribution_given_cables(4, 4, 4, 4)
        # dist[0][0] should be approximately 0.728
    """
    raise NotImplementedError("exact_distribution_given_cables not yet implemented")
