# Game Simulation Guide

## Overview

The game simulations let you experience Bombbusters from Player 0's perspective. You can see your own cables and explore probability distributions for other players using different conditional distributions from Lectures 4, 5, and 6.

## Running the Simulations

### Lecture 4: Unconditional Distribution
```bash
python lecture_04_exact_distribution/simulate_lecture_04.py
```

**What it shows:**
- Your cables (as Player 0)
- Unconditional probability distribution for any selected player
- The distribution is the same for all players (unconditional)

**Use case:** Understanding the baseline probability distribution without any conditioning.

### Lecture 5: Distribution Given Cable Count
```bash
python lecture_05_distribution_given_cable_count/simulate_lecture_05.py
```

**What it shows:**
- Your cables (as Player 0)
- Selected player's actual cables and cable count
- Conditional probability distribution given the selected player's cable count

**Use case:** Understanding how knowing a player's cable count affects the probability distribution.

### Lecture 6: Distribution Given Player Cable
```bash
python lecture_06_distribution_given_player_cable/simulate_lecture_06.py
```

**What it shows:**
- Your cables (as Player 0)
- Conditional probability distribution for other players given your actual cables
- The distribution is the same for all other players (since they're all conditioned on your cables)

**Use case:** Understanding how your specific cables affect the probability distribution for other players.

## UI Components

### Information Panel (Left)
- Shows your cables as Player 0
- Shows selected player's information
- Explains what type of distribution is being shown

### Distribution Table (Center)
- Shows probabilities for each number at each position
- Format: Percentage probabilities
- Rows: Numbers (1, 2, 3, ...)
- Columns: Positions (0, 1, 2, ...)

### Bar Chart (Bottom)
- Visual representation of the distribution
- Each bar group shows probabilities for one number
- Different colors represent different positions

### Player Selection Buttons (Bottom)
- Click to select which player to analyze
- Available players: 1, 2, 3, ... (excluding Player 0)

### New Game Button
- Click to sample a new random game
- All distributions will be recalculated

## Understanding the Distributions

### Lecture 4 (Unconditional)
- **Same for all players** - doesn't depend on which player you select
- Represents the average probability distribution
- Useful for understanding the general game dynamics

### Lecture 5 (Given Cable Count)
- **Different for each player** - depends on their cable count
- If Player 1 has 4 cables and Player 2 has 5 cables, their distributions will differ
- More specific than unconditional, but less specific than Lecture 6

### Lecture 6 (Given Player Cable)
- **Same for all other players** - all conditioned on your cables
- Most specific conditional distribution
- Shows how your specific cable combination affects probabilities
- Useful for strategic decision-making

## Tips

1. **Compare Lectures**: Run different simulations with the same game configuration to see how conditioning affects distributions
2. **Multiple Games**: Use "New Game" to see how distributions vary across different game states
3. **Player Selection**: Try selecting different players in Lecture 5 to see how cable count affects distributions
4. **Strategic Insight**: Lecture 6 is most useful for understanding how your specific situation affects other players' probabilities

## Technical Notes

- All simulations use the same game configuration (4 players, 4 numbers, 4 instances)
- Distributions are calculated using exact probability formulas (not Monte Carlo)
- Probabilities sum to 1.0 for each position
- The UI uses matplotlib for visualization

## Troubleshooting

If a simulation doesn't start:
1. Make sure all required lectures are completed (or solutions are available)
2. Check that matplotlib is installed: `pip install matplotlib`
3. Verify numpy is installed: `pip install numpy`
