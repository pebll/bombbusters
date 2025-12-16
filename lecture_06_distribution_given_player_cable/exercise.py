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

def exact_distribution_given_player_cables(P: int, N: int, M: int, player_cables: list[int]) -> list[list[float]]:
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
        
    Returns:
        Distribution matrix: result[i][j] = P(number i+1 at position j for player 1 | player 0 has player_cables)
        
    Example:
        # 4 players, 4 numbers, 4 instances each, player 0 has [1, 1, 2, 3]
        dist = exact_distribution_given_player_cables(4, 4, 4, [1, 1, 2, 3])
        # dist[0][0] should be the probability that number 1 appears at position 0 for player 1
    """
    distribution : list[list[float]] = []
    cables = starting_cables(N, M)
    print(f"Cables before: {cables}")
    for player_cable in player_cables:
        cables.remove(player_cable)
    print(f"Cables after: {cables}")
    P = P - 1 # one player already got his cables
    T = len(cables) # total cables

    c = int(T / P) # cables per player
    E = T % P # number of players with c + 1 cables
    max_positions = c if E == 0 else c+1
    # loop through all numbers
    for i in range(N):
        positions_probs: list[float] = []
        M = cables.count(i+1) # i+1 cause numbers are 1-indexed
        smaller_numbers = smaller_numbers_count(cables, i+1)
        # loop through all positions
        for j in range(max_positions):
            prob_C = position_probability_given_cables(M, T, c, j, smaller_numbers)
            prob_E = position_probability_given_cables(M, T, c+1, j, smaller_numbers)
            prob = ((P-E)/P) * prob_C + (E/P) * prob_E
            positions_probs.append(prob)
        distribution.append(positions_probs)
    return distribution

