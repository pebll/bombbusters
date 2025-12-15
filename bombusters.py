import random as rd



"""This function returns a list of players. Each player has a sorted list of numbers representing their cables"""
def sample_game(number_of_players: int, available_numbers: int, number_instances: int) -> list[list[int]]:
    # Generate cables
    cables: list[int] = []
    for n in range(available_numbers):
        for _ in range(number_instances):
            cables.append(n+1)
    rd.shuffle(cables)

    # Distribute cables to players
    #TODO: check if this works for not round result
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
        raise ValueError("WTF?")
    return players

"""This function returns the distribution of the numbers after averaged over X samples
The distribution is a list of numbers, while each number is a list of probabilities at which position it is"""
def sample_distribution(number_of_players: int, available_numbers: int, number_instances: int, num_samples: int = 100) -> list[list[float]]:
    samples: list[list[list[int]]] = []
    for _ in range(num_samples):
        samples.append(sample_game(number_of_players,    available_numbers, number_instances))
    min_cables_per_player: int = int((available_numbers * number_instances) / number_of_players)
    numbers: list[list[float]] = []
    for number in range(available_numbers):
        probs: list[float] = []
        # TODO: this will break with extra cables!
        for position in range(min_cables_per_player):
            count = 0
            for sample in samples:
                if sample[0][position] == number + 1:
                    count += 1
            probs.append(count / num_samples)
        numbers.append(probs)
    return numbers


