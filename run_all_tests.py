"""
Run all lecture tests in sequence.

This script will run tests for each lecture and stop at the first failure.
You must complete each lecture before proceeding to the next.
"""

import sys
import os
import subprocess

def run_test(lecture_name, test_file):
    """Run a test file and return success status"""
    print(f"\n{'=' * 60}")
    print(f"Running tests for {lecture_name}")
    print('=' * 60)
    
    result = subprocess.run(
        [sys.executable, test_file],
        cwd=os.path.dirname(os.path.abspath(__file__)),
        capture_output=False
    )
    
    return result.returncode == 0

def main():
    """Run all tests in sequence"""
    print("=" * 60)
    print("BOMBBUSTERS: Running All Lecture Tests")
    print("=" * 60)
    print("\nThis will run tests for each lecture in order.")
    print("You must pass all tests in a lecture before proceeding to the next.\n")
    
    lectures = [
        ("Lecture 1: Basic Combinatorics", "lecture_01_combinatorics/test_exercise.py"),
        ("Lecture 2: Hypergeometric Distribution", "lecture_02_hypergeometric/test_exercise.py"),
        ("Lecture 3: Position Probability", "lecture_03_position_probability/test_exercise.py"),
        ("Lecture 4: Exact Distribution", "lecture_04_exact_distribution/test_exercise.py"),
    ]
    
    for lecture_name, test_file in lectures:
        if not os.path.exists(test_file):
            print(f"ERROR: Test file not found: {test_file}")
            return 1
        
        success = run_test(lecture_name, test_file)
        
        if not success:
            print(f"\n{'=' * 60}")
            print(f"FAILED: {lecture_name}")
            print("=" * 60)
            print("Please fix the failing tests before proceeding to the next lecture.")
            return 1
    
    print("\n" + "=" * 60)
    print("ALL LECTURES PASSED! 🎉")
    print("=" * 60)
    print("Congratulations! You've completed the full learning path!")
    print("Run 'python main.py' to compare with Monte Carlo results.")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    exit(main())
