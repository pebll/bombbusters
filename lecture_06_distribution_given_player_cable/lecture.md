# Lecture 6: Distribution Given Player Cable

## Introduction

In this lecture, we'll calculate the probability distribution for one player **given** that we know another player's cables. This is a more complex conditional distribution where we condition on the actual cables held by one player.

## Problem Setup

We want to calculate: **P(number i appears at position j for player 1 | player 0 has specific cables)** for all numbers i and all positions j.

Given:
- `number_of_players` = P
- `available_numbers` = N
- `number_instances` = M (each number appears M times)
- `player_cables` = list of numbers representing the cables player 0 has (sorted)

## Key Insight

When we know player 0's cables, we can:
1. Remove those cables from the pool
2. Calculate the remaining cables and their distribution
3. Calculate the distribution for player 1 from the remaining pool

## The Approach

1. **Count remaining cables**: After removing player 0's cables, count how many of each number remain
2. **Calculate remaining total**: T_remaining = T - len(player_cables)
3. **Calculate remaining players**: P_remaining = P - 1
4. **Calculate cables per remaining player**: 
   - min_cables = T_remaining // P_remaining
   - extra_cables = T_remaining % P_remaining
   - c₁ = min_cables + 1 (for players with extra cable)
   - c₂ = min_cables (for other players)
5. **For each number i and position j**:
   - Calculate probability using the remaining pool
   - Weight by probability that player 1 has c₁ vs c₂ cables

## The Formula

For each number i and position j:

```
P(number i at position j for player 1 | player 0 has cables) = 
    (E_remaining/P_remaining) × P(number i at position j | c₁ cables, remaining pool) +
    ((P_remaining-E_remaining)/P_remaining) × P(number i at position j | c₂ cables, remaining pool)
```

Where:
- E_remaining = number of remaining players with extra cable
- The probability calculation uses the **remaining** pool (after removing player 0's cables)

## Implementation Steps

1. Count how many of each number remain after removing player 0's cables
2. Calculate T_remaining, P_remaining
3. Calculate c₁, c₂, E_remaining for remaining players
4. For each number i:
   - Calculate remaining instances of number i: M_remaining[i]
   - Calculate remaining smaller numbers count
   - For each position j:
     - Calculate probability for c₁ case (if position < c₁)
     - Calculate probability for c₂ case (if position < c₂)
     - Weight by (E_remaining/P_remaining) and ((P_remaining-E_remaining)/P_remaining)
5. Return the distribution

## Verification

After calculating, verify:
- Probabilities sum to 1.0 for each position
- All probabilities are between 0.0 and 1.0
- Results match Monte Carlo simulation (within sampling error)

## Example

**Setup**: 4 players, 4 numbers, 4 instances each, player 0 has [1, 1, 2, 3]

- Original pool: 4×4 = 16 cables
- Player 0 has: 1, 1, 2, 3 (4 cables)
- Remaining: 12 cables distributed among 3 players
- Each remaining player gets 4 cables (even distribution)
- Result: Distribution for player 1 given player 0's cables

## Comparison with Previous Lectures

- Lecture 4: Unconditional distribution (averaging over all possibilities)
- Lecture 5: Conditional on cable count
- Lecture 6: Conditional on actual cables of one player (most specific information)
