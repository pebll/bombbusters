# Lecture 5: Distribution Given Cable Count

## Introduction

In this lecture, we'll calculate the probability distribution **given** that we know how many cables a player has. This is a conditional distribution where we condition on the total number of positions (cables) a player receives.

## Problem Setup

We want to calculate: **P(number i appears at position j | player has c cables)** for all numbers i and all positions j.

Given:
- `number_of_players` = P
- `available_numbers` = N
- `number_instances` = M (each number appears M times)
- `cables` = c (the specific number of cables the player has)

## Key Insight

When we know a player has exactly `c` cables, we no longer need to average over the uncertainty of whether they have c₁ or c₂ cables. We can directly use `position_probability_given_cables` from Lecture 3.

## The Formula

For each number i and position j:

```
P(number i at position j | player has c cables) = 
    position_probability_given_cables(M, T, c, j, smaller_numbers_count)
```

Where:
- T = N × M (total cables)
- smaller_numbers_count = i × M (number of cables with numbers smaller than i+1)

## Implementation Steps

1. Calculate total cables: T = N × M
2. Determine max_position = c (since player has exactly c cables)
3. For each number i (0 to N-1):
   - Calculate smaller_numbers_count = i × M
   - For each position j (0 to c-1):
     - Calculate probability using `position_probability_given_cables(M, T, c, j, smaller_numbers_count)`
     - Store in `distribution[i][j]`
4. Return the distribution

## Verification

After calculating, verify:
- Probabilities sum to 1.0 for each position
- All probabilities are between 0.0 and 1.0
- Results match Monte Carlo simulation (within sampling error)

## Example

**Setup**: 4 players, 4 numbers, 4 instances each, c = 4 cables

- T = 16 cables
- Player has exactly 4 cables
- Result: A 4×4 matrix where:
  - `distribution[0][0]` ≈ 0.728 (number 1 at position 0)
  - `distribution[1][0]` ≈ 0.234 (number 2 at position 0)
  - etc.

## Comparison with Lecture 4

In Lecture 4, we averaged over the uncertainty of cable distribution. Here, we condition on a specific cable count, so the calculation is simpler - we don't need to weight by E/P and (P-E)/P.
