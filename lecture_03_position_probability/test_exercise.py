"""
Test file for Exercise 3: Position Probability

Run this to verify your implementation:
    python lecture_03_position_probability/test_exercise.py
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lecture_03_position_probability import exercise
from lecture_03_position_probability import solution


def test_position_probability_given_cables():
    """Test position_probability_given_cables function"""
    print("=" * 60)
    print("Testing position_probability_given_cables")
    print("=" * 60)
    
    # Test cases for 4 players, 4 numbers, 4 instances each (16 total cables, 4 per player)
    test_cases = [
        # (M, T, c, j, smaller_count, description)
        (4, 16, 4, 0, 0, "Number 1 at position 0"),
        (4, 16, 4, 1, 0, "Number 1 at position 1"),
        (4, 16, 4, 0, 4, "Number 2 at position 0"),
        (4, 16, 4, 3, 0, "Number 1 at position 3"),
        (4, 16, 4, 5, 0, "Invalid position (j >= c)"),
    ]
    
    all_passed = True
    for M, T, c, j, smaller_count, desc in test_cases:
        try:
            result = exercise.position_probability_given_cables(M, T, c, j, smaller_count)
            solution_result = solution.position_probability_given_cables(M, T, c, j, smaller_count)
            diff = abs(result - solution_result)
            tolerance = 1e-6
            status = "✓" if diff < tolerance else "✗"
            if diff >= tolerance:
                all_passed = False
            print(f"{status} {desc}: {result:.6f} (solution: {solution_result:.6f})")
        except NotImplementedError:
            print(f"✗ {desc} not yet implemented")
            all_passed = False
        except Exception as e:
            print(f"✗ {desc} raised exception: {e}")
            all_passed = False
    
    # Test that probabilities are valid (non-negative, reasonable)
    print("\nTesting probability validity:")
    test_validity = [
        (4, 16, 4, 0, 0),
        (4, 16, 4, 1, 0),
        (4, 16, 4, 2, 0),
        (4, 16, 4, 3, 0),
    ]
    
    for M, T, c, j, smaller_count in test_validity:
        try:
            result = exercise.position_probability_given_cables(M, T, c, j, smaller_count)
            solution_result = solution.position_probability_given_cables(M, T, c, j, smaller_count)
            
            # Check non-negative
            if result < -1e-10 or solution_result < -1e-10:
                print(f"✗ Negative probability for M={M}, T={T}, c={c}, j={j}")
                all_passed = False
                continue
            
            # Check reasonable range
            if result > 1.0 + 1e-10 or solution_result > 1.0 + 1e-10:
                print(f"✗ Probability > 1 for M={M}, T={T}, c={c}, j={j}")
                all_passed = False
                continue
            
            diff = abs(result - solution_result)
            status = "✓" if diff < 1e-6 else "✗"
            if diff >= 1e-6:
                all_passed = False
            print(f"{status} M={M}, T={T}, c={c}, j={j}: {result:.6f} (solution: {solution_result:.6f})")
        except NotImplementedError:
            print(f"✗ Validity test not yet implemented")
            all_passed = False
        except Exception as e:
            print(f"✗ Validity test raised exception: {e}")
            all_passed = False
    
    print()
    return all_passed


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("EXERCISE 3 TESTS: Position Probability")
    print("=" * 60 + "\n")
    
    results = []
    results.append(("position_probability_given_cables", test_position_probability_given_cables()))
    
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
        print("You can now proceed to Lecture 4: Exact Distribution")
    else:
        print("SOME TESTS FAILED. Please fix your implementation.")
        print("You cannot proceed to the next lecture until all tests pass.")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
