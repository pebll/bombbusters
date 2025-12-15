# Exercise 2: Hypergeometric Distribution

## Prerequisites

You must have completed Exercise 1 (Basic Combinatorics) and all tests must pass.

## Objective

Implement the `hypergeometric_probability` function using binomial coefficients.

## Task: Implement Hypergeometric Probability

Create a function `hypergeometric_probability(N: int, K: int, n: int, k: int) -> float` that calculates:

```
P(k successes) = C(K, k) × C(N-K, n-k) / C(N, n)
```

**Parameters:**
- N: Total population size
- K: Number of successes in population
- n: Sample size (number of items drawn)
- k: Number of successes in sample

**Requirements:**
1. Check for invalid inputs and return 0.0:
   - k < 0
   - k > n
   - k > K
   - (n - k) > (N - K)
2. Use `binomial_coefficient` from Lecture 1 to calculate combinations
3. Handle division by zero (when C(N, n) = 0, return 0.0)
4. Return a float (probability between 0.0 and 1.0)

**Examples:**
- Drawing 2 red balls from 5 red + 5 blue when drawing 3 total:
  ```
  hypergeometric_probability(10, 5, 3, 2) ≈ 0.4167
  ```
- Drawing 0 red balls:
  ```
  hypergeometric_probability(10, 5, 3, 0) ≈ 0.0833
  ```

**Implementation hints:**
1. Import binomial_coefficient from lecture_01_combinatorics.solution (or your exercise if you want to test your own)
2. Check all edge cases first
3. Calculate numerator = C(K, k) × C(N-K, n-k)
4. Calculate denominator = C(N, n)
5. Return numerator / denominator (handle division by zero)

## Testing

Run the test file to verify your implementation:

```bash
python lecture_02_hypergeometric/test_exercise.py
```

All tests must pass before moving to the next lecture!

## Next Steps

Once all tests pass, you can proceed to Lecture 3: Position Probability, where you'll use hypergeometric distribution to calculate position-specific probabilities.
