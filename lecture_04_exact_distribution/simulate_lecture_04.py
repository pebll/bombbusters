"""
Game Simulation for Lecture 4: Unconditional Distribution

This simulation lets you play as Player 0 and see the unconditional
probability distribution for other players.
"""

import sys
import os

# Add parent directory to path to find simulate_base
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from simulate_base import GameSimulationBase

# Try importing from exercise first, fall back to solution
try:
    from lecture_04_exact_distribution.exercise import exact_distribution
except (ImportError, NotImplementedError):
    from lecture_04_exact_distribution.solution import exact_distribution


class GameSimulationLecture04(GameSimulationBase):
    """Simulation for Lecture 4: Unconditional Distribution"""
    
    def __init__(self):
        super().__init__()
        self.distribution = None
        
    def sample_new_game(self, P=None, N=None, M=None):
        """Sample a new game and calculate unconditional distribution"""
        super().sample_new_game(P, N, M)
        # Calculate unconditional distribution (same for all players)
        self.distribution = exact_distribution(
            self.number_of_players, 
            self.available_numbers, 
            self.number_instances
        )
        self.update_display()
        
    def get_distribution(self):
        """Get the unconditional distribution (same for all players)"""
        return self.distribution
        
    def get_info_text(self):
        """Get information text for the info panel"""
        if self.game is None:
            return ""
            
        player_0_cables = self.game[0]
        info_text = f"YOU ARE PLAYER 0\n"
        info_text += f"Your cables: {player_0_cables}\n"
        info_text += f"Number of cables: {len(player_0_cables)}\n\n"
        info_text += f"Selected Player: {self.selected_player}\n"
        info_text += f"Player {self.selected_player}'s cables: {self.game[self.selected_player]}\n"
        info_text += f"Player {self.selected_player}'s cable count: {len(self.game[self.selected_player])}\n\n"
        info_text += "Distribution: UNCONDITIONAL\n"
        info_text += "(Same for all players)"
        return info_text
        
    def get_window_title(self):
        """Get the window title"""
        return 'Bombbusters Game Simulation - Lecture 4: Unconditional Distribution'


def main():
    """Main function"""
    print("=" * 60)
    print("BOMBBUSTERS GAME SIMULATION - Lecture 4")
    print("=" * 60)
    print("You are Player 0. Click buttons to view distributions for other players.")
    print("The distribution shown is UNCONDITIONAL (same for all players).")
    print("Click 'New Game' to change game parameters.")
    print()
    
    sim = GameSimulationLecture04()
    sim.create_ui()


if __name__ == "__main__":
    main()
