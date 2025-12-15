# Exercise 1: Basic Combinatorics

## Objective

Implement factorial and binomial coefficient functions.

## Task 1: Implement Factorial

Create a function `factorial(n: int) -> int` that calculates n!.

**Requirements:**
- Handle n = 0 (return 1)
- Handle n < 0 (return 0 or raise ValueError - your choice)
- Use iterative computation (don't use recursion for large n)

**Examples:**
- factorial(0) = 1
- factorial(3) = 6
- factorial(5) = 120

## Task 2: Implement Binomial Coefficient

Create a function `binomial_coefficient(n: int, k: int) -> int` that calculates C(n, k).

**Requirements:**
- Handle edge cases: k = 0, k = n, k > n, k < 0
- Use efficient computation (avoid calculating large factorials directly)
- Use symmetry property: C(n, k) = C(n, n-k) to minimize computation

**Implementation hints:**
1. Check edge cases first (k < 0, k > n → return 0; k == 0 or k == n → return 1)
2. Use symmetry: if k > n/2, compute C(n, n-k) instead
3. Compute iteratively:
   ```python
   result = 1
   for i in range(k):
       result = result * (n - i) // (i + 1)
   ```
   Note: Use integer division `//` to avoid floating point errors.

**Examples:**
- binomial_coefficient(5, 2) = 10
- binomial_coefficient(10, 0) = 1
- binomial_coefficient(10, 10) = 1
- binomial_coefficient(5, 7) = 0 (k > n)
- binomial_coefficient(6, 3) = 20

## Testing

Run the test file to verify your implementation:

```bash
python lecture_01_combinatorics/test_exercise.py
```

All tests must pass before moving to the next lecture!

## Next Steps

Once all tests pass, you can proceed to Lecture 2: Hypergeometric Distribution, where you'll use binomial coefficients to calculate probabilities.
