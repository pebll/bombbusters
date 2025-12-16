# Exercise 6: Distribution Given Player Cable

## Prerequisites

You must have completed Exercises 1, 2, 3, 4, and 5, and all tests must pass.

## Objective

Implement `exact_distribution_given_player_cables` to calculate the probability distribution for one player **given** that we know another player's actual cables.

## Task: Implement Distribution Given Player Cables

Create a function `exact_distribution_given_player_cables(number_of_players: int, available_numbers: int, number_instances: int, player_cables: list[int]) -> list[list[float]]` that:

1. Counts how many of each number remain after removing `player_cables` from the pool
2. Calculates T_remaining = T - len(player_cables)
3. Calculates P_remaining = number_of_players - 1
4. Calculates cables per remaining player:
   - min_cables = T_remaining // P_remaining
   - extra_cables = T_remaining % P_remaining
   - c₁ = min_cables + 1
   - c₂ = min_cables
   - E_remaining = extra_cables
5. For each number i (0 to available_numbers-1):
   - Calculate M_remaining[i] = number_instances - count of number (i+1) in player_cables
   - Calculate smaller_numbers_count_remaining = sum of remaining cables with numbers < (i+1)
   - For each position j (0 to max_position-1):
     - Calculate probability for c₁ case (if position < c₁ and M_remaining[i] > 0)
     - Calculate probability for c₂ case (if position < c₂ and M_remaining[i] > 0)
     - Weight by (E_remaining/P_remaining) and ((P_remaining-E_remaining)/P_remaining)
     - Store in distribution[i][j]
6. Return the distribution

**Return format**: `list[list[float]]` where `result[i][j]` is the probability that number (i+1) appears at position j for player 1, **given** that player 0 has the cables specified in `player_cables`.

**Implementation hints:**
1. Import position_probability_given_cables from lecture_03_position_probability.solution
2. Count remaining instances of each number after removing player_cables
3. Calculate remaining total and remaining players
4. Loop over numbers, then positions
5. For each (number, position) pair, calculate weighted probability using remaining pool
6. Handle edge cases: if M_remaining[i] == 0, probability should be 0.0
7. Verify probabilities sum to 1.0 for each position (optional but recommended)

**Example:**
```python
# 4 players, 4 numbers, 4 instances each, player 0 has [1, 1, 2, 3]
dist = exact_distribution_given_player_cables(4, 4, 4, [1, 1, 2, 3])
# dist[0][0] should be the probability that number 1 appears at position 0 for player 1
# given that player 0 has [1, 1, 2, 3]
```

## Testing

Run the test file to verify your implementation:

```bash
python lecture_06_distribution_given_player_cable/test_exercise.py
```

All tests must pass!

## Final Step: Compare with Monte Carlo

Once all tests pass, you can compare your exact distribution with Monte Carlo results using the conditional Monte Carlo function `sample_distribution_given_player_cables`.

## Congratulations!

You've learned how to calculate conditional distributions when we know the actual cables of one player! This is the most specific conditional distribution we can calculate.
