"""
Solution for Exercise 5: Distribution Given Cable Count
"""

from lecture_03_position_probability.solution import position_probability_given_cables


def exact_distribution_given_cables(number_of_players: int, available_numbers: int, 
                                    number_instances: int, cables: int) -> list[list[float]]:
    """
    Calculate exact probability distribution given that a player has exactly c cables.
    """
    T = available_numbers * number_instances  # Total cables
    c = cables  # Number of cables the player has
    
    # Maximum position index (player has exactly c cables, so positions 0 to c-1)
    max_position = c
    
    # Initialize result: one list per number, one probability per position
    distribution = []
    
    for number in range(available_numbers):
        probs = []
        M = number_instances  # Number of instances of this number
        # Numbers are 1-indexed (1, 2, 3, 4), so number i (0-indexed) has i numbers before it
        smaller_numbers_count = number * number_instances
        
        for position in range(max_position):
            # Calculate probability directly using position_probability_given_cables
            prob = position_probability_given_cables(M, T, c, position, smaller_numbers_count)
            probs.append(prob)
        
        distribution.append(probs)
    
    return distribution
