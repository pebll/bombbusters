"""
Test file for Exercise 6: Distribution Given Player Cable

Run this to verify your implementation:
    python lecture_06_distribution_given_player_cable/test_exercise.py
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lecture_06_distribution_given_player_cable import exercise
from lecture_06_distribution_given_player_cable import solution


def test_exact_distribution_given_player_cables():
    """Test exact_distribution_given_player_cables function"""
    print("=" * 60)
    print("Testing exact_distribution_given_player_cables")
    print("=" * 60)
    
    test_cases = [
        (4, 4, 4, [1, 1, 2, 3]),  # Standard case
        (4, 4, 4, [1, 2, 3, 4]),  # One of each number
        (3, 3, 3, [1, 1, 1]),     # All same number
        (4, 4, 4, [1, 1, 1, 1]),  # All number 1
    ]
    
    all_passed = True
    for P, N, M, player_cables in test_cases:
        try:
            result = exercise.exact_distribution_given_player_cables(P, N, M, player_cables)
            solution_result = solution.exact_distribution_given_player_cables(P, N, M, player_cables)
            
            # Check structure
            if len(result) != N:
                print(f"✗ Wrong number of numbers: {len(result)} != {N}")
                all_passed = False
                continue
            
            # Check that we have positions
            if len(result) > 0 and len(result[0]) == 0:
                print(f"✗ No positions in result")
                all_passed = False
                continue
            
            # Check probabilities sum to 1 for each position (if there are positions)
            if len(result) > 0 and len(result[0]) > 0:
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
            print(f"{status} Distribution for P={P}, N={N}, M={M}, cables={player_cables}: total diff = {diff_total:.6f}")
            
        except NotImplementedError:
            print(f"✗ Distribution for P={P}, N={N}, M={M}, cables={player_cables} not yet implemented")
            all_passed = False
        except Exception as e:
            print(f"✗ Distribution for P={P}, N={N}, M={M}, cables={player_cables} raised exception: {e}")
            import traceback
            traceback.print_exc()
            all_passed = False
    
    # Verify probabilities sum to 1.0 for each position
    print("\nVerifying probabilities sum to 1.0 for each position:")
    P, N, M, player_cables = 4, 4, 4, [1, 1, 2, 3]
    try:
        result = exercise.exact_distribution_given_player_cables(P, N, M, player_cables)
        solution_result = solution.exact_distribution_given_player_cables(P, N, M, player_cables)
        if len(result) > 0 and len(result[0]) > 0:
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
    print("EXERCISE 6 TESTS: Distribution Given Player Cable")
    print("=" * 60 + "\n")
    
    results = []
    results.append(("exact_distribution_given_player_cables", test_exact_distribution_given_player_cables()))
    
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
        print("Congratulations! You've learned the most specific conditional distributions!")
    else:
        print("SOME TESTS FAILED. Please fix your implementation.")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
