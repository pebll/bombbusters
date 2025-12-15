"""
Solution for Exercise 4: Exact Distribution
"""

from lecture_03_position_probability.solution import position_probability_given_cables


def exact_distribution(number_of_players: int, available_numbers: int, number_instances: int) -> list[list[float]]:
    """Calculate exact probability distribution"""
    T = available_numbers * number_instances  # Total cables
    P = number_of_players
    
    # Calculate cables per player (handling uneven distribution)
    min_cables_per_player = T // P
    extra_cables = T % P
    c1 = min_cables_per_player + 1  # Cables for players with extra
    c2 = min_cables_per_player       # Cables for other players
    E = extra_cables                 # Number of players with extra cable
    
    # Maximum position index (use max cables to determine)
    max_position = max(c1, c2) if extra_cables > 0 else c2
    
    # Initialize result: one list per number, one probability per position
    distribution = []
    
    for number in range(available_numbers):
        probs = []
        M = number_instances  # Number of instances of this number
        # Numbers are 1-indexed (1, 2, 3, 4), so number i (0-indexed) has i numbers before it
        smaller_numbers_count = number * number_instances
        
        for position in range(max_position):
            # Calculate probability for c1 case (players with extra cable)
            prob_c1 = 0.0
            if position < c1:
                prob_c1 = position_probability_given_cables(M, T, c1, position, smaller_numbers_count)
            
            # Calculate probability for c2 case (players without extra cable)
            prob_c2 = 0.0
            if position < c2:
                prob_c2 = position_probability_given_cables(M, T, c2, position, smaller_numbers_count)
            
            # Weight by probability of being each type of player
            # P(player 0 has c1 cables) = E / P
            # P(player 0 has c2 cables) = (P - E) / P
            if E > 0:
                total_prob = (E / P) * prob_c1 + ((P - E) / P) * prob_c2
            else:
                total_prob = prob_c2
            
            probs.append(total_prob)
        
        distribution.append(probs)
    
    return distribution
