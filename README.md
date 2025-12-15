# Bombbusters: Learning Exact Probability Calculation

A structured learning path to understand and implement exact probability calculations using combinatorics.

## Overview

This course teaches you how to replace Monte Carlo sampling with exact probability calculations. You'll learn step-by-step, building from basic combinatorics to complete distribution calculations.

## Course Structure

The course is divided into 4 progressive lectures:

1. **Lecture 1: Basic Combinatorics** - Factorials and binomial coefficients
2. **Lecture 2: Hypergeometric Distribution** - Sampling without replacement
3. **Lecture 3: Position Probability** - Calculating position-specific probabilities
4. **Lecture 4: Exact Distribution** - Complete distribution calculation

## How to Use This Course

### Prerequisites

- Python 3.7+
- Basic understanding of probability
- Familiarity with Python functions and loops

### Getting Started

1. **Start with Lecture 1**: Navigate to `lecture_01_combinatorics/`
2. **Read the lecture**: Open `lecture.md` and read through the material
3. **Read the exercise**: Open `exercise.md` for implementation instructions
4. **Implement the functions**: Edit `exercise.py` and implement the required functions
5. **Run the tests**: Execute `python lecture_01_combinatorics/test_exercise.py`
6. **Verify all tests pass**: You cannot proceed to the next lecture until all tests pass!

### Directory Structure

```
bombbusters/
├── README.md                          # This file
├── main.py                            # Final comparison script
├── base/                              # Shared utilities
│   ├── bombusters.py                 # Monte Carlo simulation functions
│   └── utils.py                      # Plotting and printing utilities
├── lecture_01_combinatorics/          # Lecture 1: Basic Combinatorics
│   ├── lecture.md                     # Lecture material
│   ├── exercise.md                    # Exercise instructions
│   ├── exercise.py                    # Your implementation (edit this!)
│   ├── solution.py                    # Reference solution (don't peek!)
│   └── test_exercise.py               # Tests (run this!)
├── lecture_02_hypergeometric/         # Lecture 2: Hypergeometric Distribution
│   ├── lecture.md
│   ├── exercise.md
│   ├── exercise.py
│   ├── solution.py
│   └── test_exercise.py
├── lecture_03_position_probability/    # Lecture 3: Position Probability
│   ├── lecture.md
│   ├── exercise.md
│   ├── exercise.py
│   ├── solution.py
│   └── test_exercise.py
└── lecture_04_exact_distribution/      # Lecture 4: Exact Distribution
    ├── lecture.md
    ├── exercise.md
    ├── exercise.py
    ├── solution.py
    └── test_exercise.py
```

### Learning Path

#### Step 1: Lecture 1 - Basic Combinatorics

```bash
# Read the lecture
cat lecture_01_combinatorics/lecture.md

# Read the exercise instructions
cat lecture_01_combinatorics/exercise.md

# Edit exercise.py and implement:
# - factorial(n)
# - binomial_coefficient(n, k)

# Run tests
python lecture_01_combinatorics/test_exercise.py
```

**Goal**: Understand factorials and binomial coefficients. All tests must pass before proceeding.

#### Step 2: Lecture 2 - Hypergeometric Distribution

```bash
# Read the lecture
cat lecture_02_hypergeometric/lecture.md

# Read the exercise instructions
cat lecture_02_hypergeometric/exercise.md

# Edit exercise.py and implement:
# - hypergeometric_probability(N, K, n, k)

# Run tests
python lecture_02_hypergeometric/test_exercise.py
```

**Goal**: Understand sampling without replacement. All tests must pass before proceeding.

#### Step 3: Lecture 3 - Position Probability

```bash
# Read the lecture
cat lecture_03_position_probability/lecture.md

# Read the exercise instructions
cat lecture_03_position_probability/exercise.md

# Edit exercise.py and implement:
# - position_probability_given_cables(M, T, c, j, smaller_numbers_count)

# Run tests
python lecture_03_position_probability/test_exercise.py
```

**Goal**: Calculate position-specific probabilities. All tests must pass before proceeding.

#### Step 4: Lecture 4 - Exact Distribution

```bash
# Read the lecture
cat lecture_04_exact_distribution/lecture.md

# Read the exercise instructions
cat lecture_04_exact_distribution/exercise.md

# Edit exercise.py and implement:
# - exact_distribution(number_of_players, available_numbers, number_instances)

# Run tests
python lecture_04_exact_distribution/test_exercise.py
```

**Goal**: Calculate complete probability distribution. All tests must pass.

#### Final Step: Compare with Monte Carlo

```bash
# Compare exact vs Monte Carlo results
python main.py
```

This will show you that your exact calculations match Monte Carlo simulation (within sampling error)!

## Important Rules

1. **Don't skip ahead**: Complete each lecture in order
2. **All tests must pass**: You cannot proceed to the next lecture until all tests pass
3. **Try first, then peek**: Try implementing yourself before looking at solutions
4. **Read the lectures**: The lectures contain important theory and examples

## Tips

- **Start simple**: Test your functions with small, known values first
- **Use the tests**: The test files show expected behavior
- **Read error messages**: They often point to the issue
- **Check edge cases**: Make sure your functions handle boundary conditions
- **Verify your math**: Print intermediate values to debug

## Troubleshooting

### Import Errors

If you get import errors, make sure you're running tests from the project root:
```bash
cd /home/lo/bombbusters
python lecture_01_combinatorics/test_exercise.py
```

### Tests Fail

- Read the error message carefully
- Check that you're handling all edge cases
- Verify your implementation matches the lecture formulas
- Compare with the solution if you're stuck (but try first!)

### Need Help?

- Re-read the lecture material
- Check the exercise hints
- Look at the solution as a last resort
- Verify your understanding of the mathematical concepts

## What You'll Learn

By the end of this course, you'll understand:

1. **Combinatorics**: How to count arrangements and combinations
2. **Hypergeometric Distribution**: Sampling without replacement
3. **Conditional Probability**: Calculating probabilities given conditions
4. **Exact Calculation**: Replacing Monte Carlo with exact formulas

## Next Steps After Completion

- Experiment with different parameters
- Compare computation time: Monte Carlo vs Exact
- Extend to other probability problems
- Apply these concepts to other domains

## Good Luck! 🎓

Take your time, understand each concept, and enjoy learning!
