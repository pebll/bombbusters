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
