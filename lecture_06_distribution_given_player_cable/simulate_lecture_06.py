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

# Try importing from exercise first, fall back to solution
try:
    from lecture_06_distribution_given_player_cable.exercise import exact_distribution_given_player_cables
except (ImportError, NotImplementedError):
    from lecture_06_distribution_given_player_cable.solution import exact_distribution_given_player_cables


class GameSimulationLecture06(GameSimulationBase):
    """Simulation for Lecture 6: Distribution Given Player Cable"""
    
    def __init__(self):
        super().__init__()
        self.distribution = None  # Distribution for other players given Player 0's cables
        
    def sample_new_game(self, P=None, N=None, M=None):
        """Sample a new game and calculate distribution given Player 0's cables"""
        super().sample_new_game(P, N, M)
        # Calculate distribution for other players given Player 0's cables
        player_0_cables = sorted(self.game[0])  # Ensure sorted
        self.distribution = exact_distribution_given_player_cables(
            self.number_of_players, 
            self.available_numbers, 
            self.number_instances, 
            player_0_cables
        )
        self.update_display()
        
    def get_distribution(self):
        """Get distribution for selected player given Player 0's cables"""
        if self.game is None:
            return None
            
        # For Player 0, show deterministic distribution (we know their cables)
        if self.selected_player == 0:
            player_0_cables = sorted(self.game[0])
            cable_count = len(player_0_cables)
            
            # Create deterministic distribution
            # For each number, probability is 1.0 at positions where it appears, 0.0 elsewhere
            # But we need to distribute probability across all positions where the number appears
            distribution = []
            for num_idx in range(self.available_numbers):
                target_num = num_idx + 1  # Convert to 1-indexed
                # Find all positions where this number appears
                positions_with_num = [pos for pos, cable in enumerate(player_0_cables) if cable == target_num]
                num_count = len(positions_with_num)
                
                probs = []
                for pos in range(cable_count):
                    if pos in positions_with_num:
                        # If number appears at this position, probability is 1.0
                        # (since we know exactly where it is)
                        probs.append(1.0)
                    else:
                        probs.append(0.0)
                distribution.append(probs)
            return distribution
        
        # For other players, use the calculated distribution
        return self.distribution
        
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
        info_text += f"Player {self.selected_player}'s cables: {selected_cables}\n"
        info_text += f"Player {self.selected_player}'s cable count: {len(selected_cables)}\n\n"
        info_text += "Distribution: CONDITIONAL\n"
        info_text += f"Given Player 0 has {player_0_cables}"
        return info_text
        
    def get_window_title(self):
        """Get the window title"""
        return 'Bombbusters Game Simulation - Lecture 6: Distribution Given Player Cable'


def main():
    """Main function"""
    print("=" * 60)
    print("BOMBBUSTERS GAME SIMULATION - Lecture 6")
    print("=" * 60)
    print("You are Player 0. Click buttons to view distributions for other players.")
    print("The distribution shown is CONDITIONAL on your actual cables.")
    print("(Same distribution applies to all other players given your cables)")
    print("Click 'New Game' to change game parameters.")
    print()
    
    sim = GameSimulationLecture06()
    sim.create_ui()


if __name__ == "__main__":
    main()
