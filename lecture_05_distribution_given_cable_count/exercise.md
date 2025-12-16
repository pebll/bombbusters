# Exercise 5: Distribution Given Cable Count

## Prerequisites

You must have completed Exercises 1, 2, 3, and 4, and all tests must pass.

## Objective

Implement `exact_distribution_given_cables` to calculate the probability distribution **given** that we know a player has exactly `c` cables.

## Task: Implement Distribution Given Cables

Create a function `exact_distribution_given_cables(number_of_players: int, available_numbers: int, number_instances: int, cables: int) -> list[list[float]]` that:

1. Calculates total cables T = available_numbers × number_instances
2. Determines max_position = cables (since player has exactly `cables` cables)
3. For each number i (0 to available_numbers-1):
   - Calculate smaller_numbers_count = i × number_instances
   - For each position j (0 to cables-1):
     - Calculate probability using `position_probability_given_cables(M, T, cables, j, smaller_numbers_count)`
     - Store in distribution[i][j]
4. Return the distribution

**Return format**: `list[list[float]]` where `result[i][j]` is the probability that number (i+1) appears at position j **given** that the player has exactly `cables` cables.

**Implementation hints:**
1. Import position_probability_given_cables from lecture_03_position_probability.solution
2. Initialize distribution as empty list
3. Loop over numbers, then positions
4. For each (number, position) pair, calculate probability directly (no weighting needed)
5. Verify probabilities sum to 1.0 for each position (optional but recommended)

**Example:**
```python
# 4 players, 4 numbers, 4 instances each, player has 4 cables
dist = exact_distribution_given_cables(4, 4, 4, 4)
# dist[0][0] should be approximately 0.728 (number 1 at position 0)
# dist[1][0] should be approximately 0.234 (number 2 at position 0)
```

## Testing

Run the test file to verify your implementation:

```bash
python lecture_05_distribution_given_cable_count/test_exercise.py
```

All tests must pass!

## Final Step: Compare with Monte Carlo

Once all tests pass, you can compare your exact distribution with Monte Carlo results using the conditional Monte Carlo function `sample_distribution_given_cables`.

## Congratulations!

You've learned how to calculate conditional distributions when we know the total number of cables a player has!
