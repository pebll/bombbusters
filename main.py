"""
Main script to compare Monte Carlo vs Exact probability distributions.

Run this after completing all lectures to see your exact calculations
match the Monte Carlo simulation!
"""

import sys
import os

# Add paths
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from base import bombusters as bb_base
from base import utils
# Import configuration
from simulation_config import (
    DEFAULT_NUMBER_OF_PLAYERS,
    DEFAULT_AVAILABLE_NUMBERS,
    DEFAULT_NUMBER_INSTANCES,
    DEFAULT_NUMBER_OF_SAMPLES
)
# Try importing from exercise first (your implementation), fall back to solution
try:
    from lecture_04_exact_distribution.exercise import exact_distribution
except (ImportError, NotImplementedError):
    from lecture_04_exact_distribution.solution import exact_distribution

# Use defaults from config file
NUMBER_OF_PLAYERS = DEFAULT_NUMBER_OF_PLAYERS
AVAILABLE_NUMBERS = DEFAULT_AVAILABLE_NUMBERS
NUMBER_INSTANCES = DEFAULT_NUMBER_INSTANCES
NUMBER_OF_SAMPLES = DEFAULT_NUMBER_OF_SAMPLES

def main():
    print("=" * 60)
    print("BOMBBUSTERS: Monte Carlo vs Exact Distribution Comparison")
    print("=" * 60)
    print(f"Configuration:")
    print(f"  Players: {NUMBER_OF_PLAYERS}")
    print(f"  Numbers: {AVAILABLE_NUMBERS}")
    print(f"  Instances per number: {NUMBER_INSTANCES}")
    print(f"  Monte Carlo samples: {NUMBER_OF_SAMPLES}")
    print()

    # Calculate Monte Carlo distribution
    print("=" * 60)
    print("MONTE CARLO DISTRIBUTION")
    print("=" * 60)
    monte_carlo_distrib = bb_base.sample_distribution(
        NUMBER_OF_PLAYERS, AVAILABLE_NUMBERS, NUMBER_INSTANCES, NUMBER_OF_SAMPLES
    )
    utils.print_distribution(monte_carlo_distrib)

    # Calculate exact distribution
    print("\n" + "=" * 60)
    print("EXACT DISTRIBUTION")
    print("=" * 60)
    exact_distrib = exact_distribution(NUMBER_OF_PLAYERS, AVAILABLE_NUMBERS, NUMBER_INSTANCES)
    utils.print_distribution(exact_distrib)

    # Compare results
    print("\n" + "=" * 60)
    print("COMPARISON (Exact - Monte Carlo)")
    print("=" * 60)
    for n, (exact_probs, mc_probs) in enumerate(zip(exact_distrib, monte_carlo_distrib)):
        diff_str = ", ".join([f"{100*(e - m):+.{1}f}%" for e, m in zip(exact_probs, mc_probs)])
        print(f"{n+1}: [{diff_str}]")

    # Verify probabilities sum to 1 for each position
    print("\n" + "=" * 60)
    print("VERIFICATION: Sum of probabilities per position (should be ~1.0)")
    print("=" * 60)
    max_positions = max(len(probs) for probs in exact_distrib)
    for pos in range(max_positions):
        sum_prob = sum(exact_distrib[n][pos] if pos < len(exact_distrib[n]) else 0.0 
                       for n in range(len(exact_distrib)))
        print(f"Position {pos}: {sum_prob:.6f}")

    # Plot both distributions
    print("\nPlotting distributions...")
    # utils.plot_distribution(monte_carlo_distrib)
    utils.plot_distribution(exact_distrib)

    print("\n" + "=" * 60)
    print("Comparison complete!")
    print("=" * 60)
    print("The exact distribution should match Monte Carlo within sampling error.")
    print("Differences are due to Monte Carlo sampling randomness.")

if __name__ == "__main__":
    main()
