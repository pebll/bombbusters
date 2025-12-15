"""
Test file for Exercise 4: Exact Distribution

Run this to verify your implementation:
    python lecture_04_exact_distribution/test_exercise.py
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lecture_04_exact_distribution import exercise
from lecture_04_exact_distribution import solution


def test_exact_distribution():
    """Test exact_distribution function"""
    print("=" * 60)
    print("Testing exact_distribution")
    print("=" * 60)
    
    test_cases = [
        (4, 4, 4),  # Standard case: even distribution
        (2, 2, 2),  # Small case
        (3, 3, 3),  # Uneven distribution case
    ]
    
    all_passed = True
    for P, N, M in test_cases:
        try:
            result = exercise.exact_distribution(P, N, M)
            solution_result = solution.exact_distribution(P, N, M)
            
            # Check structure
            if len(result) != N:
                print(f"✗ Wrong number of numbers: {len(result)} != {N}")
                all_passed = False
                continue
            
            # Check probabilities sum to 1 for each position
            max_positions = max(len(probs) for probs in result)
            for pos in range(max_positions):
                sum_prob = sum(result[n][pos] if pos < len(result[n]) else 0.0 
                              for n in range(N))
                if abs(sum_prob - 1.0) > 1e-5:
                    print(f"✗ Probabilities don't sum to 1 at position {pos}: {sum_prob}")
                    all_passed = False
            
            # Compare with solution
            max_len = max(max(len(r), len(s)) for r, s in zip(result, solution_result))
            diff_total = 0.0
            for i in range(N):
                for j in range(max_len):
                    r_val = result[i][j] if j < len(result[i]) else 0.0
                    s_val = solution_result[i][j] if j < len(solution_result[i]) else 0.0
                    diff_total += abs(r_val - s_val)
            
            tolerance = 1e-4
            status = "✓" if diff_total < tolerance else "✗"
            if diff_total >= tolerance:
                all_passed = False
            print(f"{status} Distribution for P={P}, N={N}, M={M}: total diff = {diff_total:.6f}")
            
        except NotImplementedError:
            print(f"✗ Distribution for P={P}, N={N}, M={M} not yet implemented")
            all_passed = False
        except Exception as e:
            print(f"✗ Distribution for P={P}, N={N}, M={M} raised exception: {e}")
            import traceback
            traceback.print_exc()
            all_passed = False
    
    # Verify probabilities sum to 1.0 for each position
    print("\nVerifying probabilities sum to 1.0 for each position:")
    P, N, M = 4, 4, 4
    try:
        result = exercise.exact_distribution(P, N, M)
        solution_result = solution.exact_distribution(P, N, M)
        max_positions = max(len(probs) for probs in result)
        for pos in range(max_positions):
            sum_prob = sum(result[n][pos] if pos < len(result[n]) else 0.0 
                          for n in range(N))
            solution_sum = sum(solution_result[n][pos] if pos < len(solution_result[n]) else 0.0 
                             for n in range(N))
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
    print("EXERCISE 4 TESTS: Exact Distribution")
    print("=" * 60 + "\n")
    
    results = []
    results.append(("exact_distribution", test_exact_distribution()))
    
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
        print("Congratulations! You've completed the full learning path!")
        print("Run 'python main.py' to compare with Monte Carlo results.")
    else:
        print("SOME TESTS FAILED. Please fix your implementation.")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
