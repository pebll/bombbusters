# Lecture 1: Basic Combinatorics

## Introduction

Combinatorics is the mathematics of counting arrangements. Before we can calculate exact probabilities, we need to understand how to count different arrangements.

## Factorials

The **factorial** of a positive integer n (written n!) is the product of all positive integers up to n:

```
n! = n × (n-1) × (n-2) × ... × 2 × 1
```

**Special cases:**
- 0! = 1 (by definition)
- 1! = 1

**Examples:**
- 3! = 3 × 2 × 1 = 6
- 5! = 5 × 4 × 3 × 2 × 1 = 120

**Meaning**: n! is the number of ways to arrange n distinct objects in a line.

## Binomial Coefficients

The **binomial coefficient** C(n, k) (also written as "n choose k" or `(n k)`) counts the number of ways to choose k items from n items, **without regard to order**.

**Formula:**
```
C(n, k) = n! / (k! × (n-k)!)
```

**Examples:**
- C(5, 2) = 5! / (2! × 3!) = 120 / (2 × 6) = 10
- C(10, 0) = 1 (there's exactly one way to choose nothing)
- C(10, 10) = 1 (there's exactly one way to choose everything)

**Properties:**
1. **Symmetry**: C(n, k) = C(n, n-k)
   - Example: C(10, 3) = C(10, 7) = 120
2. **Edge cases**: 
   - C(n, 0) = 1 for any n ≥ 0
   - C(n, n) = 1 for any n ≥ 0
   - C(n, k) = 0 if k > n or k < 0

**Meaning**: C(n, k) is the number of ways to choose k items from n items.

**Example**: How many ways can you choose 2 books from 5 books?
- Answer: C(5, 2) = 10 ways

## Efficient Computation

Calculating factorials directly can lead to very large numbers. Instead, we can compute binomial coefficients iteratively:

```
C(n, k) = (n × (n-1) × ... × (n-k+1)) / (k × (k-1) × ... × 1)
```

**Algorithm:**
1. Use symmetry: if k > n/2, compute C(n, n-k) instead
2. Multiply n, n-1, ..., n-k+1
3. Divide by k, k-1, ..., 1
4. Use integer division to avoid floating point errors

**Example**: C(10, 3)
- Using symmetry: C(10, 3) = C(10, 7), so use k=3 (smaller)
- Numerator: 10 × 9 × 8 = 720
- Denominator: 3 × 2 × 1 = 6
- Result: 720 / 6 = 120

## Why This Matters

Binomial coefficients are fundamental building blocks for probability calculations. They appear everywhere:
- Calculating probabilities of combinations
- Counting arrangements
- Computing distributions

In the next lecture, we'll use binomial coefficients to calculate probabilities!
