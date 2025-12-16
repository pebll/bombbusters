"""
Solution for Exercise 6: Distribution Given Player Cable
"""

from lecture_03_position_probability.solution import position_probability_given_cables


def exact_distribution_given_player_cables(number_of_players: int, available_numbers: int,
                                           number_instances: int, player_cables: list[int]) -> list[list[float]]:
    """
    Calculate exact probability distribution for player 1 given that player 0 has specific cables.
    """
    T = available_numbers * number_instances  # Total cables
    P = number_of_players
    
    # Count how many of each number remain after removing player 0's cables
    # Numbers are 1-indexed (1, 2, 3, ...), so number i (0-indexed) corresponds to number (i+1)
    remaining_instances = [number_instances] * available_numbers
    for cable in player_cables:
        if 1 <= cable <= available_numbers:
            remaining_instances[cable - 1] -= 1
    
    # Calculate remaining totals
    T_remaining = T - len(player_cables)
    P_remaining = P - 1
    
    if P_remaining <= 0:
        # No remaining players, return empty distribution
        return [[0.0] * 0 for _ in range(available_numbers)]
    
    # Calculate cables per remaining player
    min_cables_per_player = T_remaining // P_remaining
    extra_cables = T_remaining % P_remaining
    c1 = min_cables_per_player + 1  # Cables for players with extra
    c2 = min_cables_per_player       # Cables for other players
    E_remaining = extra_cables        # Number of remaining players with extra cable
    
    # Maximum position index
    max_position = max(c1, c2) if extra_cables > 0 else c2
    
    # Initialize result
    distribution = []
    
    for number in range(available_numbers):
        probs = []
        M_remaining = remaining_instances[number]  # Remaining instances of this number
        
        # Calculate remaining smaller numbers count
        # Numbers smaller than (number+1) are 1, 2, ..., number
        smaller_numbers_count_remaining = 0
        for n in range(number):
            smaller_numbers_count_remaining += remaining_instances[n]
        
        for position in range(max_position):
            # If no remaining instances of this number, probability is 0
            if M_remaining == 0:
                probs.append(0.0)
                continue
            
            # Calculate probability for c1 case (players with extra cable)
            prob_c1 = 0.0
            if position < c1:
                prob_c1 = position_probability_given_cables(
                    M_remaining, T_remaining, c1, position, smaller_numbers_count_remaining
                )
            
            # Calculate probability for c2 case (players without extra cable)
            prob_c2 = 0.0
            if position < c2:
                prob_c2 = position_probability_given_cables(
                    M_remaining, T_remaining, c2, position, smaller_numbers_count_remaining
                )
            
            # Weight by probability of being each type of player
            # P(player 1 has c1 cables) = E_remaining / P_remaining
            # P(player 1 has c2 cables) = (P_remaining - E_remaining) / P_remaining
            if E_remaining > 0:
                total_prob = (E_remaining / P_remaining) * prob_c1 + ((P_remaining - E_remaining) / P_remaining) * prob_c2
            else:
                total_prob = prob_c2
            
            probs.append(total_prob)
        
        distribution.append(probs)
    
    return distribution
