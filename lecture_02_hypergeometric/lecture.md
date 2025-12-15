# Lecture 2: Hypergeometric Distribution

## Introduction

The **hypergeometric distribution** describes the probability of getting exactly k successes when drawing n items **without replacement** from a finite population.

## Problem Setup

Imagine you have:

- A population of **N** items total
- **K** of these items are "successes" (e.g., red balls)
- **N - K** items are "failures" (e.g., blue balls)
- You draw **n** items without replacement
- What's the probability you get exactly **k** successes?

## The Formula

The probability of getting exactly k successes is:

```
P(k successes) = C(K, k) × C(N-K, n-k) / C(N, n)
```

Where C(n, k) is the binomial coefficient from Lecture 1.

**Breaking it down:**

- **C(K, k)**: Ways to choose k successes from K available successes
- **C(N-K, n-k)**: Ways to choose (n-k) failures from (N-K) available failures
- **C(N, n)**: Total ways to choose n items from N items

## Example

**Problem**: You have 10 balls: 5 red and 5 blue. You draw 3 balls without replacement. What's the probability you get exactly 2 red balls?

**Solution**:

- N = 10 (total balls)
- K = 5 (red balls = successes)
- n = 3 (balls drawn)
- k = 2 (red balls we want)

```
P(2 red) = C(5, 2) × C(5, 1) / C(10, 3)
         = 10 × 5 / 120
         = 50 / 120
         = 5/12
         ≈ 0.4167
```

- N = 10 (total balls)
- K = 5 (red balls = successes)
- n = 1 (balls drawn)
- k = 1 (red balls we want)

```
P(2 red) = C(5, 1) × C(5, 0) / C(10, 1)
         = (5! / (1! * 4!)) * 1 / 10 
         = 5 / 10
         = 0.5 -> expected
```

## Properties

1. **Valid range**: k must satisfy:
   - k ≥ 0
   - k ≤ n
   - k ≤ K
   - (n - k) ≤ (N - K)

2. **Probability sum**: For fixed N, K, n, the sum of P(k) over all valid k equals 1.0

3. **Edge cases**:
   - If k is outside the valid range, P(k) = 0
   - If n = 0, then P(0) = 1 and P(k) = 0 for k > 0

## Why This Matters

In bombbusters, we use hypergeometric distribution to calculate:

- Probability a player gets exactly k cables of a specific number
- This is the foundation for calculating position probabilities

## Next Steps

In Lecture 3, we'll use hypergeometric distribution to calculate the probability that a specific number appears at a specific position!
