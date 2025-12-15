# Quick Start Guide

## Fast Track to Learning

Follow these steps to complete the course:

### 1. Lecture 1: Basic Combinatorics

```bash
# Read the material
cat lecture_01_combinatorics/lecture.md
cat lecture_01_combinatorics/exercise.md

# Implement in exercise.py
# - factorial(n)
# - binomial_coefficient(n, k)

# Test
python lecture_01_combinatorics/test_exercise.py
```

**Must pass all tests before proceeding!**

### 2. Lecture 2: Hypergeometric Distribution

```bash
# Read the material
cat lecture_02_hypergeometric/lecture.md
cat lecture_02_hypergeometric/exercise.md

# Implement in exercise.py
# - hypergeometric_probability(N, K, n, k)

# Test
python lecture_02_hypergeometric/test_exercise.py
```

**Must pass all tests before proceeding!**

### 3. Lecture 3: Position Probability

```bash
# Read the material
cat lecture_03_position_probability/lecture.md
cat lecture_03_position_probability/exercise.md

# Implement in exercise.py
# - position_probability_given_cables(M, T, c, j, smaller_numbers_count)

# Test
python lecture_03_position_probability/test_exercise.py
```

**Must pass all tests before proceeding!**

### 4. Lecture 4: Exact Distribution

```bash
# Read the material
cat lecture_04_exact_distribution/lecture.md
cat lecture_04_exact_distribution/exercise.md

# Implement in exercise.py
# - exact_distribution(number_of_players, available_numbers, number_instances)

# Test
python lecture_04_exact_distribution/test_exercise.py
```

**Must pass all tests!**

### 5. Final Comparison

```bash
# Compare exact vs Monte Carlo
python main.py
```

## Running All Tests

To run all tests at once (stops at first failure):

```bash
python run_all_tests.py
```

## File Structure

Each lecture folder contains:
- `lecture.md` - Theory and explanations
- `exercise.md` - Implementation instructions
- `exercise.py` - **Your code goes here!**
- `solution.py` - Reference solution (don't peek!)
- `test_exercise.py` - Tests to verify your implementation

## Key Rules

1. ✅ Complete lectures in order
2. ✅ All tests must pass before moving to next lecture
3. ✅ Try implementing yourself before looking at solutions
4. ✅ Read the lecture material - it contains important theory

## Need Help?

- Re-read the lecture material
- Check exercise hints
- Look at solution as last resort
- Verify your understanding of the math

Good luck! 🎓
