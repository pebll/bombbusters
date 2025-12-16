# Game Simulation Plan

## Overview
Create interactive game simulations where the user plays as Player 0 and can see probability distributions for other players using different conditional distributions from Lectures 4, 5, and 6.

## Structure

### Three Simulation Scripts (one per lecture)

1. **`lecture_04_exact_distribution/simulate_lecture_04.py`** - Unconditional Distribution
   - Uses `exact_distribution()` from Lecture 4
   - Shows distribution for any player without conditioning
   - User sees: Player 0's cables + distribution for selected player (unconditional)

2. **`lecture_05_distribution_given_cable_count/simulate_lecture_05.py`** - Distribution Given Cable Count
   - Uses `exact_distribution_given_cable_count()` from Lecture 5
   - Shows distribution for selected player given their cable count
   - User sees: Player 0's cables + selected player's cable count + distribution

3. **`lecture_06_distribution_given_player_cable/simulate_lecture_06.py`** - Distribution Given Player Cable
   - Uses `exact_distribution_given_player_cable()` from Lecture 6
   - Shows distribution for selected player given Player 0's actual cables
   - User sees: Player 0's cables + distribution for selected player (conditioned on Player 0's cables)

## UI Components

### Common Elements (all simulations):
- **Game State Display**: Show Player 0's cables (sorted list)
- **Player Selection**: Buttons or dropdown to select which player to analyze (1, 2, 3, ...)
- **Distribution Visualization**: 
  - Table showing probabilities for each number at each position
  - Bar chart or heatmap visualization
  - Summary statistics

### Lecture-Specific Elements:

**Lecture 4:**
- Show: "Unconditional distribution for Player X"
- No additional information needed

**Lecture 5:**
- Show: "Distribution for Player X given they have Y cables"
- Display: Selected player's cable count
- Calculate distribution using `exact_distribution_given_cable_count(P, N, M, cables)`

**Lecture 6:**
- Show: "Distribution for Player X given Player 0 has [cables]"
- Display: Player 0's cables prominently
- Calculate distribution using `exact_distribution_given_player_cable(P, N, M, player_0_cables)`

## Implementation Details

### Data Flow:
1. Sample a game using `sample_game(P, N, M)`
2. Extract Player 0's cables: `game[0]`
3. For each other player:
   - Lecture 4: Calculate `exact_distribution(P, N, M)` (same for all players)
   - Lecture 5: Calculate `exact_distribution_given_cable_count(P, N, M, len(game[player_idx]))`
   - Lecture 6: Calculate `exact_distribution_given_player_cable(P, N, M, game[0])`

### UI Framework:
- Use matplotlib for visualization (consistent with existing codebase)
- Interactive buttons for player selection
- Display distribution as:
  - Table (numbers × positions)
  - Bar chart (per number, showing position probabilities)
  - Summary text

### File Structure:
```
simulate_base.py (in root)
lecture_04_exact_distribution/simulate_lecture_04.py
lecture_05_distribution_given_cable_count/simulate_lecture_05.py
lecture_06_distribution_given_player_cable/simulate_lecture_06.py
```

Each file will:
- Import necessary functions from respective lectures
- Sample a game
- Create interactive matplotlib UI
- Allow player selection and display distributions

## User Experience Flow

1. Run simulation script (e.g., `python lecture_04_exact_distribution/simulate_lecture_04.py`)
2. See Player 0's cables displayed
3. See list of other players
4. Click/select a player to see their distribution
5. View distribution table and visualization
6. Option to resample game or exit

## Technical Considerations

- Handle edge cases (e.g., all cables of one number taken)
- Ensure probabilities sum to 1.0 for each position
- Display probabilities as percentages for readability
- Make UI responsive and clear
- Use consistent styling across all three simulations
