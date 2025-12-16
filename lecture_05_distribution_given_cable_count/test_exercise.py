"""
Test file for Exercise 5: Distribution Given Cable Count

Run this to verify your implementation:
    python lecture_05_distribution_given_cable_count/test_exercise.py
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lecture_05_distribution_given_cable_count import exercise
from lecture_05_distribution_given_cable_count import solution


def test_exact_distribution_given_cable_count():
    """Test exact_distribution_given_cables function"""
    print("=" * 60)
    print("Testing exact_distribution_given_cables")
    print("=" * 60)
    
    test_cases = [
        (4, 4, 4, 4),  # Standard case: even distribution, 4 cables
        (4, 4, 4, 5),  # Standard case: even distribution, 5 cables (extra cable)
        (3, 3, 3, 3),  # Small case, 3 cables
        (3, 3, 3, 4),  # Small case, 4 cables (extra cable)
    ]
    
    all_passed = True
    for P, N, M, c in test_cases:
        try:
            result = exercise.exact_distribution_given_cable_count(P, N, M, c)
            solution_result = solution.exact_distribution_given_cable_count(P, N, M, c)
            
            # Check structure
            if len(result) != N:
                print(f"✗ Wrong number of numbers: {len(result)} != {N}")
                all_passed = False
                continue
            
            # Check that we have the right number of positions
            if len(result[0]) != c:
                print(f"✗ Wrong number of positions: {len(result[0])} != {c}")
                all_passed = False
                continue
            
            # Check probabilities sum to 1 for each position
            for pos in range(c):
                sum_prob = sum(result[n][pos] for n in range(N))
                if abs(sum_prob - 1.0) > 1e-5:
                    print(f"✗ Probabilities don't sum to 1 at position {pos}: {sum_prob}")
                    all_passed = False
            
            # Compare with solution
            diff_total = 0.0
            for i in range(N):
                for j in range(c):
                    diff_total += abs(result[i][j] - solution_result[i][j])
            
            tolerance = 1e-4
            status = "✓" if diff_total < tolerance else "✗"
            if diff_total >= tolerance:
                all_passed = False
            print(f"{status} Distribution for P={P}, N={N}, M={M}, c={c}: total diff = {diff_total:.6f}")
            
        except NotImplementedError:
            print(f"✗ Distribution for P={P}, N={N}, M={M}, c={c} not yet implemented")
            all_passed = False
        except Exception as e:
            print(f"✗ Distribution for P={P}, N={N}, M={M}, c={c} raised exception: {e}")
            import traceback
            traceback.print_exc()
            all_passed = False
    
    # Verify probabilities sum to 1.0 for each position
    print("\nVerifying probabilities sum to 1.0 for each position:")
    P, N, M, c = 4, 4, 4, 4
    try:
        result = exercise.exact_distribution_given_cable_count(P, N, M, c)
        solution_result = solution.exact_distribution_given_cable_count(P, N, M, c)
        for pos in range(c):
            sum_prob = sum(result[n][pos] for n in range(N))
            solution_sum = sum(solution_result[n][pos] for n in range(N))
            diff = abs(sum_prob - 1.0)
            diff_solution = abs(sum_prob - solution_sum)
            tolerance = 1e-5
            status = "✓" if diff < tolerance and diff_solution < tolerance else "✗"
            if diff >= tolerance or diff_solution >= tolerance:
                all_passed = False
            print(f"{status} Position {pos}: sum = {sum_prob:.10f} (solution: {solution_sum:.10f})")
    except NotImplementedError:
        print("✗ Sum verification not yet implemented")
        all_passed = False
    except Exception as e:
        print(f"✗ Sum verification raised exception: {e}")
        all_passed = False
    
    print()
    return all_passed


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("EXERCISE 5 TESTS: Distribution Given Cable Count")
    print("=" * 60 + "\n")
    
    results = []
    results.append(("exact_distribution_given_cables", test_exact_distribution_given_cable_count()))
    
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
        print("Congratulations! You've learned conditional distributions!")
    else:
        print("SOME TESTS FAILED. Please fix your implementation.")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
