# Project Structure

## Overview

This project is organized as a progressive learning path with 4 self-contained lectures. Each lecture builds on the previous one, and you must complete all tests before proceeding.

## Directory Structure

```
bombbusters/
├── README.md                    # Main instructions
├── QUICK_START.md              # Quick reference guide
├── STRUCTURE.md                # This file
├── main.py                     # Final comparison script
├── run_all_tests.py            # Run all tests in sequence
│
├── base/                       # Shared utilities (used by all lectures)
│   ├── __init__.py
│   ├── bombusters.py          # Monte Carlo simulation functions
│   └── utils.py               # Plotting and printing utilities
│
├── lecture_01_combinatorics/  # Lecture 1: Basic Combinatorics
│   ├── lecture.md             # Theory and explanations
│   ├── exercise.md            # Implementation instructions
│   ├── exercise.py            # YOUR CODE - implement here!
│   ├── solution.py            # Reference solution (don't peek!)
│   ├── test_exercise.py       # Tests (run this!)
│   └── __init__.py
│
├── lecture_02_hypergeometric/ # Lecture 2: Hypergeometric Distribution
│   ├── lecture.md
│   ├── exercise.md
│   ├── exercise.py            # YOUR CODE - implement here!
│   ├── solution.py
│   ├── test_exercise.py
│   └── __init__.py
│
├── lecture_03_position_probability/  # Lecture 3: Position Probability
│   ├── lecture.md
│   ├── exercise.md
│   ├── exercise.py            # YOUR CODE - implement here!
│   ├── solution.py
│   ├── test_exercise.py
│   └── __init__.py
│
└── lecture_04_exact_distribution/    # Lecture 4: Exact Distribution
    ├── lecture.md
    ├── exercise.md
    ├── exercise.py            # YOUR CODE - implement here!
    ├── solution.py
    ├── test_exercise.py
    └── __init__.py
```

## Lecture Dependencies

Each lecture depends on the previous ones:

- **Lecture 1**: No dependencies (foundation)
- **Lecture 2**: Depends on Lecture 1 (uses `binomial_coefficient`)
- **Lecture 3**: Depends on Lecture 2 (uses `hypergeometric_probability`)
- **Lecture 4**: Depends on Lecture 3 (uses `position_probability_given_cables`)

## File Types

### Lecture Files (`lecture.md`)
- Theory and mathematical background
- Examples and explanations
- Key concepts and formulas

### Exercise Files (`exercise.md`)
- Step-by-step instructions
- Implementation requirements
- Hints and tips

### Implementation Files (`exercise.py`)
- **This is where you write your code!**
- Contains function stubs with `NotImplementedError`
- Replace stubs with your implementation

### Solution Files (`solution.py`)
- Complete working implementation
- Reference for checking your work
- **Don't look until you've tried yourself!**

### Test Files (`test_exercise.py`)
- Comprehensive test suite
- Compares your implementation vs solution
- **All tests must pass before proceeding!**

## Workflow

1. **Read** `lecture.md` - Understand the theory
2. **Read** `exercise.md` - Understand what to implement
3. **Edit** `exercise.py` - Write your implementation
4. **Run** `test_exercise.py` - Verify your code works
5. **Repeat** until all tests pass
6. **Move** to next lecture

## Key Principles

1. **Self-contained**: Each lecture folder has everything needed
2. **Progressive**: Each lecture builds on previous knowledge
3. **Test-driven**: Tests verify correctness before proceeding
4. **Isolated**: Solutions don't interfere with your work
5. **Shared base**: Common utilities in `base/` folder

## Import Strategy

Exercise files try to import from previous lectures' exercise files first (your implementation), falling back to solutions if not implemented:

```python
# Example from lecture_02_hypergeometric/exercise.py
try:
    from lecture_01_combinatorics.exercise import binomial_coefficient
except (ImportError, NotImplementedError):
    from lecture_01_combinatorics.solution import binomial_coefficient
```

This allows you to use your own implementations once they pass tests!

## Testing Strategy

- Each lecture has its own test file
- Tests compare your implementation vs solution
- Tests verify edge cases and correctness
- **All tests must pass** before proceeding

## Final Verification

After completing all lectures:
- Run `python main.py` to compare exact vs Monte Carlo
- Results should match within sampling error
- Probabilities should sum to 1.0 for each position

## Notes

- Old lecture files in root (`lecture_01_combinatorics.md`, etc.) are kept for reference
- You can ignore them and focus on the new structured lectures
- The `base/` folder contains shared utilities used by all lectures
