"""
Test file for Exercise 2: Hypergeometric Distribution

Run this to verify your implementation:
    python lecture_02_hypergeometric/test_exercise.py
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lecture_02_hypergeometric import exercise
from lecture_02_hypergeometric import solution


def test_hypergeometric_probability():
    """Test hypergeometric_probability function"""
    print("=" * 60)
    print("Testing hypergeometric_probability")
    print("=" * 60)
    
    # Known test case: Drawing 2 red balls from 5 red + 5 blue when drawing 3 total
    # C(5,2) * C(5,1) / C(10,3) = 10 * 5 / 120 = 50/120 = 5/12 ≈ 0.4167
    test_cases = [
        (10, 5, 3, 2, 0.4166666666666667),  # 2 red from 5 red + 5 blue, draw 3
        (10, 5, 3, 0, 0.08333333333333333),  # 0 red
        (10, 5, 3, 3, 0.08333333333333333),  # 3 red
        (10, 5, 3, 5, 0.0),  # Invalid: k > n
        (10, 5, 3, -1, 0.0),  # Invalid: k < 0
        (20, 10, 5, 3, 0.360),  # Approximate
    ]
    
    all_passed = True
    for N, K, n, k, expected in test_cases:
        try:
            result = exercise.hypergeometric_probability(N, K, n, k)
            solution_result = solution.hypergeometric_probability(N, K, n, k)
            # Allow small floating point differences
            diff = abs(result - expected)
            diff_solution = abs(result - solution_result)
            tolerance = 1e-6
            status = "✓" if diff < tolerance and diff_solution < tolerance else "✗"
            if diff >= tolerance or diff_solution >= tolerance:
                all_passed = False
            print(f"{status} P(k={k} | N={N}, K={K}, n={n}) = {result:.6f} (expected {expected:.6f}, solution {solution_result:.6f})")
        except NotImplementedError:
            print(f"✗ P(k={k} | N={N}, K={K}, n={n}) not yet implemented")
            all_passed = False
        except Exception as e:
            print(f"✗ P(k={k} | N={N}, K={K}, n={n}) raised exception: {e}")
            all_passed = False
    
    # Test that probabilities sum to 1.0
    print("\nTesting probability sums (should sum to 1.0):")
    test_sums = [
        (10, 5, 3),  # Draw 3 from 10 with 5 successes
        (20, 10, 5),  # Draw 5 from 20 with 10 successes
    ]
    
    for N, K, n in test_sums:
        try:
            total = sum(exercise.hypergeometric_probability(N, K, n, k) 
                       for k in range(max(0, n - (N - K)), min(n, K) + 1))
            solution_total = sum(solution.hypergeometric_probability(N, K, n, k) 
                                for k in range(max(0, n - (N - K)), min(n, K) + 1))
            diff = abs(total - 1.0)
            diff_solution = abs(total - solution_total)
            tolerance = 1e-6
            status = "✓" if diff < tolerance and diff_solution < tolerance else "✗"
            if diff >= tolerance or diff_solution >= tolerance:
                all_passed = False
            print(f"{status} Sum for N={N}, K={K}, n={n} = {total:.10f} (solution: {solution_total:.10f})")
        except NotImplementedError:
            print(f"✗ Sum test not yet implemented")
            all_passed = False
        except Exception as e:
            print(f"✗ Sum test raised exception: {e}")
            all_passed = False
    
    print()
    return all_passed


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("EXERCISE 2 TESTS: Hypergeometric Distribution")
    print("=" * 60 + "\n")
    
    results = []
    results.append(("hypergeometric_probability", test_hypergeometric_probability()))
    
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
        print("You can now proceed to Lecture 3: Position Probability")
    else:
        print("SOME TESTS FAILED. Please fix your implementation.")
        print("You cannot proceed to the next lecture until all tests pass.")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
