"""
Base module with shared Monte Carlo simulation functions.
These functions are used across all lectures for comparison and testing.
"""

import random as rd


def sample_game(number_of_players: int, available_numbers: int, number_instances: int) -> list[list[int]]:
    """
    Simulate one game of bombbusters.
    
    Returns a list of players. Each player has a sorted list of numbers representing their cables.
    """
    # Generate cables
    cables: list[int] = []
    for n in range(available_numbers):
        for _ in range(number_instances):
            cables.append(n+1)
    rd.shuffle(cables)

    # Distribute cables to players
    players: list[list[int]] = [[] for _ in range(number_of_players)]
    min_cables_per_player: int = int((available_numbers * number_instances) / number_of_players)
    extra_cables = (available_numbers * number_instances) % number_of_players
    for p in range(number_of_players):
        count = min_cables_per_player + 1 if p < extra_cables else min_cables_per_player
        for _ in range(count):
            players[p].append(cables.pop())
    rd.shuffle(players)

    # Sort cables
    for p in range(number_of_players):
        players[p].sort()

    if cables:
        raise ValueError("There is still a cable after all cables have been distributed!")
    if len(players) != number_of_players:
        raise ValueError("Invalid number of players!")
    return players


def sample_distribution(number_of_players: int, available_numbers: int, number_instances: int, num_samples: int = 100) -> list[list[float]]:
    """
    Estimate probability distribution using Monte Carlo sampling.
    
    Returns the distribution of numbers after averaging over num_samples games.
    The distribution is a list of numbers, while each number is a list of probabilities at which position it is.
    """
    samples: list[list[list[int]]] = []
    for _ in range(num_samples):
        samples.append(sample_game(number_of_players, available_numbers, number_instances))
    min_cables_per_player: int = int((available_numbers * number_instances) / number_of_players)
    numbers: list[list[float]] = []
    for number in range(available_numbers):
        probs: list[float] = []
        for position in range(min_cables_per_player):
            count = 0
            for sample in samples:
                if sample[0][position] == number + 1:
                    count += 1
            probs.append(count / num_samples)
        numbers.append(probs)
    return numbers


def sample_distribution_given_cables(number_of_players: int, available_numbers: int, 
                                     number_instances: int, cables: int, 
                                     num_samples: int = 1000) -> list[list[float]]:
    """
    Estimate probability distribution using Monte Carlo sampling, conditioned on player 0 having exactly 'cables' cables.
    
    Returns the distribution of numbers after averaging over num_samples games where player 0 has exactly 'cables' cables.
    The distribution is a list of numbers, while each number is a list of probabilities at which position it is.
    
    Args:
        number_of_players: Number of players
        available_numbers: Number of different numbers
        number_instances: Number of instances of each number
        cables: Exact number of cables player 0 must have
        num_samples: Target number of valid samples (may need more games to get this many valid samples)
    
    Returns:
        Distribution matrix: result[i][j] = P(number i+1 at position j | player 0 has exactly 'cables' cables)
    """
    samples: list[list[list[int]]] = []
    attempts = 0
    max_attempts = num_samples * 10  # Prevent infinite loops
    
    # Collect samples where player 0 has exactly 'cables' cables
    while len(samples) < num_samples and attempts < max_attempts:
        attempts += 1
        game = sample_game(number_of_players, available_numbers, number_instances)
        if len(game[0]) == cables:
            samples.append(game)
    
    if len(samples) == 0:
        # No valid samples found, return zeros
        return [[0.0] * cables for _ in range(available_numbers)]
    
    numbers: list[list[float]] = []
    for number in range(available_numbers):
        probs: list[float] = []
        for position in range(cables):
            count = 0
            for sample in samples:
                if position < len(sample[0]) and sample[0][position] == number + 1:
                    count += 1
            probs.append(count / len(samples))
        numbers.append(probs)
    return numbers


def sample_distribution_given_player_cables(number_of_players: int, available_numbers: int,
                                           number_instances: int, player_cables: list[int],
                                           num_samples: int = 1000) -> list[list[float]]:
    """
    Estimate probability distribution using Monte Carlo sampling, conditioned on player 0 having specific cables.
    
    Returns the distribution of numbers for player 1 after averaging over num_samples games where player 0 
    has exactly the cables specified in player_cables (sorted).
    
    The distribution is a list of numbers, while each number is a list of probabilities at which position it is.
    
    Args:
        number_of_players: Number of players
        available_numbers: Number of different numbers
        number_instances: Number of instances of each number
        player_cables: Sorted list of numbers representing player 0's cables
        num_samples: Target number of valid samples (may need more games to get this many valid samples)
    
    Returns:
        Distribution matrix: result[i][j] = P(number i+1 at position j for player 1 | player 0 has player_cables)
    """
    # Sort player_cables to ensure consistent comparison
    expected_cables = sorted(player_cables)
    
    samples: list[list[list[int]]] = []
    attempts = 0
    max_attempts = num_samples * 20  # Prevent infinite loops, may need more attempts for specific cables
    
    # Collect samples where player 0 has exactly the specified cables
    while len(samples) < num_samples and attempts < max_attempts:
        attempts += 1
        game = sample_game(number_of_players, available_numbers, number_instances)
        if game[0] == expected_cables:
            samples.append(game)
    
    if len(samples) == 0:
        # No valid samples found, calculate max positions from remaining cables
        T_remaining = (available_numbers * number_instances) - len(player_cables)
        P_remaining = number_of_players - 1
        if P_remaining > 0:
            max_positions = T_remaining // P_remaining + (1 if T_remaining % P_remaining > 0 else 0)
        else:
            max_positions = 0
        return [[0.0] * max_positions for _ in range(available_numbers)]
    
    # Calculate max positions from remaining cables
    T_remaining = (available_numbers * number_instances) - len(player_cables)
    P_remaining = number_of_players - 1
    if P_remaining > 0:
        min_cables = T_remaining // P_remaining
        extra_cables = T_remaining % P_remaining
        max_positions = min_cables + 1 if extra_cables > 0 else min_cables
    else:
        max_positions = 0
    
    numbers: list[list[float]] = []
    for number in range(available_numbers):
        probs: list[float] = []
        for position in range(max_positions):
            count = 0
            for sample in samples:
                # Check player 1 (index 1) since we're conditioning on player 0
                if len(sample) > 1 and position < len(sample[1]) and sample[1][position] == number + 1:
                    count += 1
            probs.append(count / len(samples))
        numbers.append(probs)
    return numbers
