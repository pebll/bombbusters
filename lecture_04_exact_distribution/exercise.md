# Exercise 4: Exact Distribution

## Prerequisites

You must have completed Exercises 1, 2, and 3, and all tests must pass.

## Objective

Implement `exact_distribution` to calculate the complete probability distribution for all numbers and all positions, handling uneven cable distribution.

## Task: Implement Exact Distribution

Create a function `exact_distribution(number_of_players: int, available_numbers: int, number_instances: int) -> list[list[float]]` that:

1. Calculates total cables T = available_numbers × number_instances
2. Calculates cables per player (handling uneven distribution):
   - min_cables_per_player = T // number_of_players
   - extra_cables = T % number_of_players
   - c₁ = min_cables_per_player + 1 (for players with extra cable)
   - c₂ = min_cables_per_player (for other players)
   - E = extra_cables (number of players with extra cable)
3. Determines max_position (maximum number of positions to consider)
4. For each number i (0 to available_numbers-1):
   - Calculate smaller_numbers_count = i × number_instances
   - For each position j (0 to max_position-1):
     - Calculate probability for c₁ case (if position < c₁)
     - Calculate probability for c₂ case (if position < c₂)
     - Weight by (E/P) and ((P-E)/P) respectively
     - Store in distribution[i][j]
5. Return the distribution

**Return format**: `list[list[float]]` where `result[i][j]` is the probability that number (i+1) appears at position j for player 0.

**Implementation hints:**
1. Import position_probability_given_cables from lecture_03_position_probability.solution
2. Initialize distribution as empty list
3. Loop over numbers, then positions
4. For each (number, position) pair, calculate weighted probability
5. Verify probabilities sum to 1.0 for each position (optional but recommended)

**Example:**
```python
# 4 players, 4 numbers, 4 instances each
dist = exact_distribution(4, 4, 4)
# dist[0][0] should be approximately 0.728 (number 1 at position 0)
# dist[1][0] should be approximately 0.234 (number 2 at position 0)
```

## Testing

Run the test file to verify your implementation:

```bash
python lecture_04_exact_distribution/test_exercise.py
```

All tests must pass!

## Final Step: Compare with Monte Carlo

Once all tests pass, run the main comparison script:

```bash
python main.py
```

This will compare your exact distribution with Monte Carlo results. They should match closely (within sampling error)!

## Congratulations!

You've completed the full learning path! You now understand:
- Basic combinatorics (factorials, binomial coefficients)
- Hypergeometric distribution
- Position-specific probability calculation
- Complete exact distribution calculation

You can now use exact probability calculations instead of Monte Carlo sampling!
