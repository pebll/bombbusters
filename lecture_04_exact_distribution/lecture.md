# Lecture 4: Exact Distribution

## Introduction

Now we'll calculate the complete probability distribution for all numbers and all positions, handling uneven cable distribution among players.

## Problem Setup

We want to calculate: **P(number i appears at position j for player 0)** for all numbers i and all positions j.

Given:

- `number_of_players` = P
- `available_numbers` = N
- `number_instances` = M (each number appears M times)
- Total cables = T = N × M

## Handling Uneven Distribution

If T is not evenly divisible by P:

- Some players get **c₁ = ⌊T/P⌋ + 1** cables (players with extra cable)
- Others get **c₂ = ⌊T/P⌋** cables
- Number of players with extra cable: **E = T mod P**

Since players are shuffled randomly, player 0 is equally likely to be any player:

- P(player 0 has c₁ cables) = E / P
- P(player 0 has c₂ cables) = (P - E) / P

## The Complete Formula

For each number i and position j:

```
P(number i at position j) = 
    (E/P) × P(number i at position j | c₁ cables) +
    ((P-E)/P) × P(number i at position j | c₂ cables)
```

Where P(number i at position j | c cables) is calculated using `position_probability_given_cables` from Lecture 3.

## Implementation Steps

1. Calculate total cables: T = N × M
2. Calculate cables per player:
   - min_cables_per_player = T // P
   - extra_cables = T % P
   - c₁ = min_cables_per_player + 1
   - c₂ = min_cables_per_player
   - E = extra_cables
3. Determine max_position (maximum number of positions to consider)
4. For each number i (0 to N-1):
   - Calculate smaller_numbers_count = i × M
   - For each position j (0 to max_position-1):
     - Calculate probability for c₁ case (if position < c₁)
     - Calculate probability for c₂ case (if position < c₂)
     - Weight by (E/P) and ((P-E)/P) respectively
     - Store in `distribution[i][j]`
5. Return the distribution

## Verification

After calculating, verify:

- Probabilities sum to 1.0 for each position
- All probabilities are between 0.0 and 1.0
- Results match Monte Carlo simulation (within sampling error)

## Example

**Setup**: 4 players, 4 numbers, 4 instances each

- T = 16 cables
- Each player gets exactly 4 cables (even distribution)
- E = 0, so all players have c₂ = 4 cables

**Result**: A 4×4 matrix where:

- `distribution[0][0]` ≈ 0.728 (number 1 at position 0)
- `distribution[1][0]` ≈ 0.234 (number 2 at position 0)
- etc.

## Congratulations

You've now implemented the complete exact probability calculation! You can compare it with Monte Carlo results and see that they match (within sampling error).
