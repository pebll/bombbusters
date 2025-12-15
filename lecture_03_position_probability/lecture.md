# Lecture 3: Position Probability

## Introduction

Now we'll calculate the probability that a specific number appears at a specific position in a player's sorted cable list.

## Problem Setup

Given:
- A player receives exactly **c** cables
- We want to know: **P(number i at position j)**
- After receiving cables, the player **sorts them** (this is crucial!)

## Key Insight: Sorting Matters!

After sorting, cables are arranged in order. If a player has:
- **s** cables of numbers < i (smaller numbers)
- **k** cables of number i
- **(c - s - k)** cables of numbers > i (larger numbers)

Then the sorted order is:
```
[smaller numbers] + [number i repeated k times] + [larger numbers]
```

So number i occupies positions **s** through **s+k-1**.

## The Formula

For number i to appear at position j, we need:
- **s ≤ j < s+k** (position j must be within the range where number i appears)

We sum over all valid combinations:

```
P(number i at position j | player has c cables) = 
    Σ_{k=1}^{min(M, c)} Σ_{s=max(0, j-k+1)}^{min(j, c-k)}
        P(s cables of smaller numbers) × P(k cables of i | s smaller cables)
```

Where:
- **M** = number of instances of number i in the deck
- **T** = total cables
- **c** = number of cables the player receives
- **j** = position index (0-indexed)
- **smaller_numbers_count** = total number of cables with numbers < i

## Step-by-Step Calculation

For each valid (s, k) pair:

1. **P(s cables of smaller numbers)**:
   ```
   hypergeometric_probability(T, smaller_count, c, s)
   ```
   - Population: T cables
   - Successes: smaller_count cables
   - Draw: c cables
   - Want: s successes

2. **P(k cables of i | s smaller cables)**:
   ```
   hypergeometric_probability(T - smaller_count, M, c - s, k)
   ```
   - Population: remaining cables (T - smaller_count)
   - Successes: M cables of number i
   - Draw: remaining cables (c - s)
   - Want: k successes

3. **Multiply and sum**: Add up all valid combinations

## Example

**Setup**: 4 players, 4 numbers, 4 instances each (total 16 cables)
- Each player gets 4 cables
- We want: P(number 1 at position 0)

**Calculation**:
- M = 4 (instances of number 1)
- T = 16 (total cables)
- c = 4 (cables per player)
- j = 0 (position)
- smaller_count = 0 (no numbers smaller than 1)

For k = 1, 2, 3, 4:
- s must be 0 (since j = 0 and s ≤ j)
- Calculate P(0 smaller) × P(k of number 1 | 0 smaller)
- Sum them up

Result: ≈ 0.728 (number 1 is very likely at position 0!)

## Next Steps

In Lecture 4, we'll extend this to calculate the full distribution for all numbers and all positions, handling uneven cable distribution!
