# Exercise 3: Position Probability

## Prerequisites

You must have completed Exercises 1 and 2, and all tests must pass.

## Objective

Implement `position_probability_given_cables` to calculate the probability that a specific number appears at a specific position, given that a player receives exactly c cables.

## Task: Implement Position Probability

Create a function `position_probability_given_cables(M: int, T: int, c: int, j: int, smaller_numbers_count: int) -> float` that calculates:

```
P(number i at position j | player has c cables)
```

**Parameters:**
- M: Number of instances of number i in the deck
- T: Total number of cables
- c: Number of cables the player receives
- j: Position index (0-indexed)
- smaller_numbers_count: Total number of cables with numbers < i

**Requirements:**
1. Check edge cases: if j >= c or c <= 0, return 0.0
2. Sum over all possible k (number of cables of number i): k from 1 to min(M, c)
3. For each k, sum over all valid s (number of smaller cables):
   - s_min = max(0, j - k + 1)
   - s_max = min(j, c - k)
4. For each (s, k) pair:
   - Calculate P(s cables of smaller numbers) using hypergeometric_probability
   - Calculate P(k cables of i | s smaller cables) using hypergeometric_probability
   - Multiply and add to total probability

**Implementation hints:**
1. Import hypergeometric_probability from lecture_02_hypergeometric.solution
2. Initialize probability = 0.0
3. Loop over k from 1 to min(M, c)
4. For each k, calculate valid s range
5. Loop over s in that range
6. Calculate both probabilities and multiply, add to total
7. Return total probability

**Example:**
```python
# 4 players, 4 numbers, 4 instances each
# Each player gets 4 cables
# P(number 1 at position 0)
position_probability_given_cables(M=4, T=16, c=4, j=0, smaller_numbers_count=0)
# Should be approximately 0.728
```

## Testing

Run the test file to verify your implementation:

```bash
python lecture_03_position_probability/test_exercise.py
```

All tests must pass before moving to the next lecture!

## Next Steps

Once all tests pass, you can proceed to Lecture 4: Exact Distribution, where you'll calculate the full probability distribution for all numbers and positions.
