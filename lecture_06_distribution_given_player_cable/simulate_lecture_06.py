"""
Game Simulation for Lecture 6: Distribution Given Player Cable

This simulation lets you play as Player 0 and see the probability
distribution for other players given your actual cables.
"""

import sys
import os

# Add parent directory to path to find simulate_base
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from simulate_base import GameSimulationBase
import matplotlib.pyplot as plt

# Try importing from exercise first, fall back to solution
try:
    from lecture_06_distribution_given_player_cable.exercise import exact_distribution_given_player_cables
except (ImportError, NotImplementedError):
    from lecture_06_distribution_given_player_cable.solution import exact_distribution_given_player_cables

# Import exercise 5 for Player 0 distribution
try:
    from lecture_05_distribution_given_cable_count.exercise import exact_distribution_given_cable_count
except (ImportError, NotImplementedError):
    from lecture_05_distribution_given_cable_count.solution import exact_distribution_given_cable_count


class GameSimulationLecture06(GameSimulationBase):
    """Simulation for Lecture 6: Distribution Given Player Cable"""
    
    def __init__(self):
        super().__init__()
        
    def sample_new_game(self, P=None, N=None, M=None):
        """Sample a new game"""
        super().sample_new_game(P, N, M)
        self.update_display()
        
    def get_distribution(self):
        """Get distribution for selected player given Player 0's cables"""
        if self.game is None:
            return None
            
        player_0_cables = sorted(self.game[0])  # Ensure sorted
        
        # For Player 0, show distribution from exercise 5 (distribution given cable count)
        # This shows how random/possible their draw was
        if self.selected_player == 0:
            cable_count = len(player_0_cables)
            
            # Use exercise 5: distribution given cable count
            distribution = exact_distribution_given_cable_count(
                self.number_of_players,
                self.available_numbers,
                self.number_instances,
                cable_count
            )
            return distribution
        
        # For other players, calculate distribution using their actual cable count
        selected_player_cables = self.game[self.selected_player]
        cable_count = len(selected_player_cables)
        
        distribution = exact_distribution_given_player_cables(
            self.number_of_players, 
            self.available_numbers, 
            self.number_instances, 
            player_0_cables,
            c=cable_count  # Pass the selected player's cable count
        )
        return distribution
        
    def get_info_text(self):
        """Get information text for the info panel"""
        if self.game is None:
            return ""
            
        player_0_cables = sorted(self.game[0])
        selected_cables = self.game[self.selected_player]
        
        info_text = f"YOU ARE PLAYER 0\n"
        info_text += f"Your cables: {player_0_cables}\n"
        info_text += f"Number of cables: {len(player_0_cables)}\n\n"
        info_text += f"Selected Player: {self.selected_player}\n"
        if self.selected_player == 0:
            info_text += f"Distribution: EXERCISE 5\n"
            info_text += f"Distribution given cable count ({len(player_0_cables)})\n"
            info_text += f"This shows how random/possible your draw was"
        else:
            info_text += f"Player {self.selected_player}'s cables: {selected_cables}\n"
            info_text += f"Player {self.selected_player}'s cable count: {len(selected_cables)}\n\n"
            info_text += "Distribution: CONDITIONAL\n"
            info_text += f"Given Player 0 has {player_0_cables}"
            info_text += f"\nAND Player {self.selected_player} has {len(selected_cables)} cables"
        return info_text
        
    def get_window_title(self):
        """Get the window title"""
        return 'Bombbusters Game Simulation - Lecture 6: Distribution Given Player Cable'
    
    def update_display(self):
        """Update the display with Player 0 band and current game state"""
        # Call parent update first
        super().update_display()
        
        # Add Player 0 band at the top (below title)
        if self.game is not None and self.fig is not None:
            player_0_cables = sorted(self.game[0])
            # Create a text annotation at the top of the figure (below suptitle)
            player_0_text = f"Player 0 (YOU): {player_0_cables}"
            self.fig.text(0.5, 0.96, player_0_text, 
                         ha='center', va='top',
                         fontsize=11, fontweight='bold',
                         bbox=dict(boxstyle='round,pad=0.4', 
                                  facecolor='lightblue', 
                                  alpha=0.85,
                                  edgecolor='darkblue',
                                  linewidth=2))
            plt.draw()


def main():
    """Main function"""
    print("=" * 60)
    print("BOMBBUSTERS GAME SIMULATION - Lecture 6")
    print("=" * 60)
    print("You are Player 0. Click buttons to view distributions for other players.")
    print("The distribution shown is CONDITIONAL on your actual cables")
    print("AND the selected player's cable count.")
    print("Click 'New Game' to change game parameters.")
    print()
    
    sim = GameSimulationLecture06()
    sim.create_ui()


if __name__ == "__main__":
    main()
