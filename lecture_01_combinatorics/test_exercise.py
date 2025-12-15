"""
Test file for Exercise 1: Basic Combinatorics

Run this to verify your implementation:
    python lecture_01_combinatorics/test_exercise.py
"""

import sys
import os

# Add parent directory to path to import exercise and solution
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lecture_01_combinatorics import exercise
from lecture_01_combinatorics import solution


def test_factorial():
    """Test factorial function"""
    print("=" * 60)
    print("Testing factorial")
    print("=" * 60)
    
    test_cases = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (10, 3628800),
    ]
    
    all_passed = True
    for n, expected in test_cases:
        try:
            result = exercise.factorial(n)
            solution_result = solution.factorial(n)
            status = "✓" if result == expected == solution_result else "✗"
            if result != expected or result != solution_result:
                all_passed = False
            print(f"{status} factorial({n}) = {result} (expected {expected}, solution {solution_result})")
        except NotImplementedError:
            print(f"✗ factorial({n}) not yet implemented")
            all_passed = False
        except Exception as e:
            print(f"✗ factorial({n}) raised exception: {e}")
            all_passed = False
    
    # Test edge case
    try:
        result = exercise.factorial(-1)
        solution_result = solution.factorial(-1)
        status = "✓" if result == solution_result else "✗"
        if result != solution_result:
            all_passed = False
        print(f"{status} factorial(-1) = {result} (solution {solution_result})")
    except NotImplementedError:
        print(f"✗ factorial(-1) not yet implemented")
        all_passed = False
    except Exception as e:
        print(f"✗ factorial(-1) raised exception: {e}")
        all_passed = False
    
    print()
    return all_passed


def test_binomial_coefficient():
    """Test binomial_coefficient function"""
    print("=" * 60)
    print("Testing binomial_coefficient")
    print("=" * 60)
    
    test_cases = [
        (5, 2, 10),
        (10, 0, 1),
        (10, 10, 1),
        (5, 7, 0),  # k > n
        (10, -1, 0),  # k < 0
        (0, 0, 1),
        (6, 3, 20),
        (10, 5, 252),
        (15, 7, 6435),
    ]
    
    all_passed = True
    for n, k, expected in test_cases:
        try:
            result = exercise.binomial_coefficient(n, k)
            solution_result = solution.binomial_coefficient(n, k)
            status = "✓" if result == expected == solution_result else "✗"
            if result != expected or result != solution_result:
                all_passed = False
            print(f"{status} C({n}, {k}) = {result} (expected {expected}, solution {solution_result})")
        except NotImplementedError:
            print(f"✗ C({n}, {k}) not yet implemented")
            all_passed = False
        except Exception as e:
            print(f"✗ C({n}, {k}) raised exception: {e}")
            all_passed = False
    
    # Test symmetry property
    print("\nTesting symmetry property C(n, k) = C(n, n-k):")
    symmetry_tests = [(10, 3), (15, 7), (20, 5)]
    for n, k in symmetry_tests:
        try:
            c1 = exercise.binomial_coefficient(n, k)
            c2 = exercise.binomial_coefficient(n, n - k)
            solution_c1 = solution.binomial_coefficient(n, k)
            solution_c2 = solution.binomial_coefficient(n, n - k)
            status = "✓" if c1 == c2 == solution_c1 == solution_c2 else "✗"
            if c1 != c2 or c1 != solution_c1:
                all_passed = False
            print(f"{status} C({n}, {k}) = {c1}, C({n}, {n-k}) = {c2} (solution: {solution_c1}, {solution_c2})")
        except NotImplementedError:
            print(f"✗ Symmetry test for C({n}, {k}) not yet implemented")
            all_passed = False
        except Exception as e:
            print(f"✗ Symmetry test raised exception: {e}")
            all_passed = False
    
    print()
    return all_passed


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("EXERCISE 1 TESTS: Basic Combinatorics")
    print("=" * 60 + "\n")
    
    results = []
    results.append(("factorial", test_factorial()))
    results.append(("binomial_coefficient", test_binomial_coefficient()))
    
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    for name, passed in results:
        status = "PASSED ✓" if passed else "FAILED ✗"
        print(f"{name:40s} {status}")
    
    all_passed = all(passed for _, passed in results)
    print("=" * 60)
    if all_passed:
        print("ALL TESTS PASSED! 🎉")
        print("You can now proceed to Lecture 2: Hypergeometric Distribution")
    else:
        print("SOME TESTS FAILED. Please fix your implementation.")
        print("You cannot proceed to the next lecture until all tests pass.")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
