"""
Game Simulation for Lecture 5: Distribution Given Cable Count

This simulation lets you play as Player 0 and see the probability
distribution for other players given their cable count.
"""

import sys
import os

# Add parent directory to path to find simulate_base
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from simulate_base import GameSimulationBase

# Try importing from exercise first, fall back to solution
try:
    from lecture_05_distribution_given_cable_count.exercise import exact_distribution_given_cable_count
except (ImportError, NotImplementedError):
    from lecture_05_distribution_given_cable_count.solution import exact_distribution_given_cable_count


class GameSimulationLecture05(GameSimulationBase):
    """Simulation for Lecture 5: Distribution Given Cable Count"""
    
    def __init__(self):
        super().__init__()
        self.distributions = {}  # Cache distributions by cable count
        
    def sample_new_game(self, P=None, N=None, M=None):
        """Sample a new game and clear distribution cache"""
        super().sample_new_game(P, N, M)
        self.distributions = {}
        self.update_display()
        
    def get_distribution(self):
        """Get distribution for selected player given their cable count"""
        if self.game is None or self.selected_player < 0 or self.selected_player >= self.number_of_players:
            return None
            
        cable_count = len(self.game[self.selected_player])
        
        # Cache distributions by cable count
        if cable_count not in self.distributions:
            self.distributions[cable_count] = exact_distribution_given_cable_count(
                self.number_of_players, 
                self.available_numbers, 
                self.number_instances, 
                cable_count
            )
        
        return self.distributions[cable_count]
        
    def get_info_text(self):
        """Get information text for the info panel"""
        if self.game is None:
            return ""
            
        player_0_cables = self.game[0]
        selected_cables = self.game[self.selected_player]
        cable_count = len(selected_cables)
        
        info_text = f"YOU ARE PLAYER 0\n"
        info_text += f"Your cables: {player_0_cables}\n"
        info_text += f"Number of cables: {len(player_0_cables)}\n\n"
        info_text += f"Selected Player: {self.selected_player}\n"
        info_text += f"Player {self.selected_player}'s cables: {selected_cables}\n"
        info_text += f"Player {self.selected_player}'s cable count: {cable_count}\n\n"
        info_text += "Distribution: CONDITIONAL\n"
        info_text += f"Given Player {self.selected_player} has {cable_count} cables"
        return info_text
        
    def get_window_title(self):
        """Get the window title"""
        return 'Bombbusters Game Simulation - Lecture 5: Distribution Given Cable Count'


def main():
    """Main function"""
    print("=" * 60)
    print("BOMBBUSTERS GAME SIMULATION - Lecture 5")
    print("=" * 60)
    print("You are Player 0. Click buttons to view distributions for other players.")
    print("The distribution shown is CONDITIONAL on the selected player's cable count.")
    print("Click 'New Game' to change game parameters.")
    print()
    
    sim = GameSimulationLecture05()
    sim.create_ui()


if __name__ == "__main__":
    main()
