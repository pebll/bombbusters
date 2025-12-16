"""
Exercise 6: Distribution Given Player Cable

Implement exact_distribution_given_player_cables function.
"""

# Import position_probability_given_cables from Lecture 3
# Try importing from exercise first (your implementation), fall back to solution
try:
    from lecture_03_position_probability.exercise import position_probability_given_cables
except (ImportError, NotImplementedError):
    from lecture_03_position_probability.solution import position_probability_given_cables

def starting_cables(N: int, M: int) -> list[int]:
    cables = []
    for i in range(N):
        for _ in range(M):
            cables.append(i+1)
    return cables

def smaller_numbers_count(cables: list[int], i: int) -> int:
    cables.sort()
    count = 0
    for number in cables:
        if number == i:
            break
        count += 1
    return count

def exact_distribution_given_player_cables(P: int, N: int, M: int, player_cables: list[int], c: int|None = None) -> list[list[float]]:
    """
    Calculate exact probability distribution for player 1 given that player 0 has specific cables.
    
    Returns the same format as sample_distribution:
    list[list[float]] where result[i][j] is the probability that 
    number (i+1) appears at position j for player 1, given that player 0 has the cables
    specified in player_cables.
    
    Args:
        number_of_players: Number of players (P)
        available_numbers: Number of different numbers (N)
        number_instances: Number of instances of each number (M)
        player_cables: Sorted list of numbers representing player 0's cables
        c: Optional cable count for player 1. If provided, calculates distribution assuming
           player 1 has exactly c cables. If None, averages over all possible cable counts.
        
    Returns:
        Distribution matrix: result[i][j] = P(number i+1 at position j for player 1 | player 0 has player_cables)
        If c is provided, this is conditional on player 1 having exactly c cables.
        
    Example:
        # 4 players, 4 numbers, 4 instances each, player 0 has [1, 1, 2, 3]
        # Without cable count (averages over all possible cable counts)
        dist = exact_distribution_given_player_cables(4, 4, 4, [1, 1, 2, 3])
        # With cable count (assumes player 1 has exactly 4 cables)
        dist = exact_distribution_given_player_cables(4, 4, 4, [1, 1, 2, 3], c=4)
    """
    distribution : list[list[float]] = []
    cables = starting_cables(N, M)
    for player_cable in player_cables:
        cables.remove(player_cable)
    P = P - 1 # one player already got his cables
    T = len(cables) # total cables remaining
    # Original behavior: average over all possible cable counts
    c_min = int(T / P) # cables per player (minimum)
    E = T % P # number of players with c_min + 1 cables
    max_positions = c_min if E == 0 else c_min+1
    max_positions = c if c else max_positions
    # loop through all numbers
    for i in range(N):
        positions_probs: list[float] = []
        M = cables.count(i+1) # i+1 cause numbers are 1-indexed
        smaller_numbers = smaller_numbers_count(cables, i+1)
        # loop through all positions
        for j in range(max_positions):
            if c:
                prob = position_probability_given_cables(M, T, c, j, smaller_numbers)
            else:
                prob_C = position_probability_given_cables(M, T, c_min, j, smaller_numbers)
                prob_E = position_probability_given_cables(M, T, c_min+1, j, smaller_numbers)
                prob = ((P-E)/P) * prob_C + (E/P) * prob_E
            positions_probs.append(prob)
        distribution.append(positions_probs)
    return distribution

