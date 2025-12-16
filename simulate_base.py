"""
Base class for Bombbusters game simulations.

This class provides common functionality for all lecture-specific simulations.
Subclasses should override abstract methods to provide lecture-specific behavior.
"""

import sys
import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import numpy as np
from abc import ABC, abstractmethod

# Add paths
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from base import bombusters as bb_base

# Import default configuration
try:
    from simulation_config import (
        DEFAULT_NUMBER_OF_PLAYERS,
        DEFAULT_AVAILABLE_NUMBERS,
        DEFAULT_NUMBER_INSTANCES
    )
except ImportError:
    # Fallback defaults if config file doesn't exist
    DEFAULT_NUMBER_OF_PLAYERS = 4
    DEFAULT_AVAILABLE_NUMBERS = 4
    DEFAULT_NUMBER_INSTANCES = 4


class GameSimulationBase(ABC):
    """Base class for game simulations"""
    
    def __init__(self):
        """Initialize the simulation"""
        self.game = None
        self.selected_player = 0  # Start with Player 0 (you)
        self.fig = None
        self.ax_overview = None
        self.ax_detail = None
        
        # Game parameters (can be changed)
        self.number_of_players = DEFAULT_NUMBER_OF_PLAYERS
        self.available_numbers = DEFAULT_AVAILABLE_NUMBERS
        self.number_instances = DEFAULT_NUMBER_INSTANCES
        
        # Admin view toggle
        self.admin_view = False
        self.admin_button = None
        
        # View mode: 'number' or 'position'
        self.view_mode = 'position'  # 'number' shows number across positions, 'position' shows numbers at position
        self.view_mode_button = None
        
    @abstractmethod
    def get_distribution(self):
        """
        Get the distribution for the currently selected player.
        
        Returns:
            list[list[float]]: Distribution matrix, or None if not available
        """
        pass
        
    @abstractmethod
    def get_info_text(self):
        """
        Get the information text to display in the info panel.
        
        Returns:
            str: Information text
        """
        pass
        
    @abstractmethod
    def get_window_title(self):
        """
        Get the window title.
        
        Returns:
            str: Window title
        """
        pass
        
    def sample_new_game(self, P=None, N=None, M=None):
        """
        Sample a new game with optional parameters.
        
        Args:
            P: Number of players (uses current if None)
            N: Available numbers (uses current if None)
            M: Number of instances (uses current if None)
        """
        if P is not None:
            self.number_of_players = P
        if N is not None:
            self.available_numbers = N
        if M is not None:
            self.number_instances = M
            
        self.game = bb_base.sample_game(
            self.number_of_players, 
            self.available_numbers, 
            self.number_instances
        )
        self.selected_player = 0  # Start with Player 0 (you)
        self.update_display()
        
    def update_display(self):
        """Update the display with current game state and selected player's distribution"""
        if self.game is None:
            return
        
        # Don't update if UI hasn't been created yet
        if self.ax_overview is None or self.ax_detail is None:
            return
            
        distribution = self.get_distribution()
        if distribution is None:
            return
            
        # Clear axes
        self.ax_overview.clear()
        self.ax_detail.clear()
        
        # Store distribution early for admin info display
        self._current_distribution = distribution
        
        # Overview plot (top) - line plot with all distributions
        for n, probs in enumerate(distribution):
            x = list(range(len(probs)))
            self.ax_overview.plot(x, probs, marker='o', label=f'Number {n+1}', linewidth=2)
        
        # Title with "(you)" for Player 0
        player_label = f"Player {self.selected_player} (you)" if self.selected_player == 0 else f"Player {self.selected_player}"
        title = f"Overview - All Distributions for {player_label}"
        if self.admin_view and self.selected_player != 0:
            title += " [ADMIN VIEW]"
        self.ax_overview.set_title(title, fontsize=14, fontweight='bold')
        self.ax_overview.set_xlabel("Position")
        self.ax_overview.set_ylabel("Probability")
        self.ax_overview.set_ylim(0, 1)
        self.ax_overview.legend()
        self.ax_overview.grid(True, alpha=0.3)
        
        # Show actual cables: always for Player 0, or when admin view is ON for other players
        if self.selected_player == 0:
            # Always show admin markers for Player 0 (you)
            if self.game is not None:
                self._show_admin_info()
        elif self.admin_view:
            # Show admin markers for other players only when admin view is ON
            if self.game is not None:
                self._show_admin_info()
                self._show_all_players_info()
        
        # Detail plot (bottom) - depends on view mode
        if self.view_mode == 'number':
            # Number view: show selected number across positions
            selected_num = 0
            probs = distribution[selected_num] if distribution else []
            x = list(range(len(probs)))
            bars = self.ax_detail.bar(x, probs, color='steelblue', edgecolor='black')
            
            # Add percentage labels
            for i, p in enumerate(probs):
                if p > 0.01:  # Only show if > 1%
                    self.ax_detail.text(i, p, f'{100*p:.1f}%', 
                                  ha='center', va='bottom', fontweight='bold')
            
            # Title with "(you)" for Player 0
            player_label = f"Player {self.selected_player} (you)" if self.selected_player == 0 else f"Player {self.selected_player}"
            detail_title = f"Number {selected_num+1} - Detailed View ({player_label})"
            if self.admin_view and self.selected_player != 0:
                detail_title += " [ADMIN VIEW]"
            self.ax_detail.set_title(detail_title, fontsize=14, fontweight='bold')
            self.ax_detail.set_xlabel("Position")
            self.ax_detail.set_ylabel("Probability")
            if probs:
                self.ax_detail.set_ylim(0, max(probs) * 1.15)
            self.ax_detail.set_xticks(x)
            self.ax_detail.grid(True, alpha=0.3, axis='y')
            
            # Show actual cables in detail view: always for Player 0, or when admin view is ON
            if self.selected_player == 0:
                # Always show for Player 0
                if self.game is not None:
                    self._show_admin_detail(selected_num)
            elif self.admin_view:
                # Show for other players only when admin view is ON
                if self.game is not None:
                    self._show_admin_detail(selected_num)
            
            self._selected_number = selected_num
            self._selected_position = 0  # Reset position selection
        else:
            # Position view: show all numbers at selected position
            selected_pos = 0
            max_positions = max(len(probs) for probs in distribution) if distribution else 0
            if selected_pos < max_positions:
                # Get probabilities for all numbers at this position
                pos_probs = [dist[selected_pos] if selected_pos < len(dist) else 0.0 
                            for dist in distribution]
                x = np.arange(len(pos_probs))
                bars = self.ax_detail.bar(x, pos_probs, color='steelblue', edgecolor='black')
                
                # Add percentage labels
                for i, p in enumerate(pos_probs):
                    if p > 0.01:  # Only show if > 1%
                        self.ax_detail.text(i, p, f'{100*p:.1f}%', 
                                      ha='center', va='bottom', fontweight='bold')
                
                # Title with "(you)" for Player 0
                player_label = f"Player {self.selected_player} (you)" if self.selected_player == 0 else f"Player {self.selected_player}"
                detail_title = f"Position {selected_pos} - Detailed View ({player_label})"
                if self.admin_view and self.selected_player != 0:
                    detail_title += " [ADMIN VIEW]"
                self.ax_detail.set_title(detail_title, fontsize=14, fontweight='bold')
                self.ax_detail.set_xlabel("Number")
                self.ax_detail.set_ylabel("Probability")
                if pos_probs:
                    self.ax_detail.set_ylim(0, max(pos_probs) * 1.15)
                self.ax_detail.set_xticks(x)
                self.ax_detail.set_xticklabels([f"{i+1}" for i in range(len(pos_probs))])
                self.ax_detail.grid(True, alpha=0.3, axis='y')
                
                # Show actual cable in detail view: always for Player 0, or when admin view is ON
                if self.selected_player == 0:
                    # Always show for Player 0
                    if self.game is not None:
                        self._show_admin_position_detail(selected_pos)
                elif self.admin_view:
                    # Show for other players only when admin view is ON
                    if self.game is not None:
                        self._show_admin_position_detail(selected_pos)
            
            self._selected_position = selected_pos
            self._selected_number = 0  # Reset number selection
        
        # Distribution already stored earlier for admin info
        
        # Create/update selection buttons based on view mode
        # Clean up first to prevent conflicts
        self._cleanup_all_buttons()
        
        if self.view_mode == 'number':
            self._create_number_buttons()
        else:
            self._create_position_buttons()
        
        plt.draw()
        
    def _cleanup_all_buttons(self):
        """Clean up all selection buttons to prevent conflicts"""
        # Clean up number buttons
        for btn in self._num_buttons:
            try:
                if hasattr(btn, 'disconnect_events'):
                    btn.disconnect_events()
                if hasattr(btn, 'ax') and btn.ax is not None:
                    try:
                        btn.ax.remove()
                    except:
                        pass
            except:
                pass
        self._num_buttons = []
        
        # Clean up position buttons
        for btn in self._pos_buttons:
            try:
                if hasattr(btn, 'disconnect_events'):
                    btn.disconnect_events()
                if hasattr(btn, 'ax') and btn.ax is not None:
                    try:
                        btn.ax.remove()
                    except:
                        pass
            except:
                pass
        self._pos_buttons = []
        
        # Force a small pause to let matplotlib clean up
        plt.pause(0.01)
    
    def _create_number_buttons(self):
        """Create or update number selection buttons"""
        # First clean up all buttons to prevent conflicts
        self._cleanup_all_buttons()
        
        if not hasattr(self, '_current_distribution') or not self._current_distribution:
            return
            
        num_distributions = len(self._current_distribution)
        
        # Create buttons for each number
        for i in range(num_distributions):
            btn_ax = plt.axes([0.1 + i*0.08, 0.08, 0.07, 0.03])
            num_btn = Button(btn_ax, f'N{i+1}')
            self._num_buttons.append(num_btn)
            
            def make_num_callback(idx):
                def callback(event):
                    self.select_number(idx)
                return callback
            
            num_btn.on_clicked(make_num_callback(i))
    
    def _create_position_buttons(self):
        """Create or update position selection buttons"""
        # First clean up all buttons to prevent conflicts
        self._cleanup_all_buttons()
        
        if not hasattr(self, '_current_distribution') or not self._current_distribution:
            return
            
        # Find max positions
        max_positions = max(len(probs) for probs in self._current_distribution) if self._current_distribution else 0
        
        # Create buttons for each position
        for i in range(max_positions):
            btn_ax = plt.axes([0.1 + i*0.08, 0.08, 0.07, 0.03])
            pos_btn = Button(btn_ax, f'P{i}')
            self._pos_buttons.append(pos_btn)
            
            def make_pos_callback(idx):
                def callback(event):
                    self.select_position(idx)
                return callback
            
            pos_btn.on_clicked(make_pos_callback(i))
        
    def select_player(self, player_idx):
        """Select a player to view"""
        if player_idx < 0 or player_idx >= self.number_of_players:
            return
        self.selected_player = player_idx
        self.update_display()
        
    def select_number(self, num_idx):
        """Select a number to view in detail (number view mode)"""
        if not hasattr(self, '_current_distribution') or self._current_distribution is None:
            return
        if num_idx < 0 or num_idx >= len(self._current_distribution):
            return
        
        if self.view_mode != 'number':
            return
            
        self._selected_number = num_idx
        probs = self._current_distribution[num_idx]
        x = list(range(len(probs)))
        
        self.ax_detail.clear()
        self.ax_detail.bar(x, probs, color='steelblue', edgecolor='black')
        
        for i, p in enumerate(probs):
            if p > 0.01:
                self.ax_detail.text(i, p, f'{100*p:.1f}%', 
                              ha='center', va='bottom', fontweight='bold')
        
        # Title with "(you)" for Player 0
        player_label = f"Player {self.selected_player} (you)" if self.selected_player == 0 else f"Player {self.selected_player}"
        detail_title = f"Number {num_idx+1} - Detailed View ({player_label})"
        if self.admin_view and self.selected_player != 0:
            detail_title += " [ADMIN VIEW]"
        self.ax_detail.set_title(detail_title, fontsize=14, fontweight='bold')
        self.ax_detail.set_xlabel("Position")
        self.ax_detail.set_ylabel("Probability")
        if probs:
            self.ax_detail.set_ylim(0, max(probs) * 1.15)
        self.ax_detail.set_xticks(x)
        self.ax_detail.grid(True, alpha=0.3, axis='y')
        
        # Show actual cables in detail view: always for Player 0, or when admin view is ON
        if self.selected_player == 0:
            # Always show for Player 0
            if self.game is not None:
                self._show_admin_detail(num_idx)
        elif self.admin_view:
            # Show for other players only when admin view is ON
            if self.game is not None:
                self._show_admin_detail(num_idx)
            
        plt.draw()
    
    def select_position(self, pos_idx):
        """Select a position to view in detail (position view mode)"""
        if not hasattr(self, '_current_distribution') or self._current_distribution is None:
            return
        
        if self.view_mode != 'position':
            return
        
        max_positions = max(len(probs) for probs in self._current_distribution) if self._current_distribution else 0
        if pos_idx < 0 or pos_idx >= max_positions:
            return
            
        self._selected_position = pos_idx
        
        # Get probabilities for all numbers at this position
        pos_probs = [dist[pos_idx] if pos_idx < len(dist) else 0.0 
                    for dist in self._current_distribution]
        x = np.arange(len(pos_probs))
        
        self.ax_detail.clear()
        self.ax_detail.bar(x, pos_probs, color='steelblue', edgecolor='black')
        
        for i, p in enumerate(pos_probs):
            if p > 0.01:
                self.ax_detail.text(i, p, f'{100*p:.1f}%', 
                              ha='center', va='bottom', fontweight='bold')
        
        # Title with "(you)" for Player 0
        player_label = f"Player {self.selected_player} (you)" if self.selected_player == 0 else f"Player {self.selected_player}"
        detail_title = f"Position {pos_idx} - Detailed View ({player_label})"
        if self.admin_view and self.selected_player != 0:
            detail_title += " [ADMIN VIEW]"
        self.ax_detail.set_title(detail_title, fontsize=14, fontweight='bold')
        self.ax_detail.set_xlabel("Number")
        self.ax_detail.set_ylabel("Probability")
        if pos_probs:
            self.ax_detail.set_ylim(0, max(pos_probs) * 1.15)
        self.ax_detail.set_xticks(x)
        self.ax_detail.set_xticklabels([f"{i+1}" for i in range(len(pos_probs))])
        self.ax_detail.grid(True, alpha=0.3, axis='y')
        
        # Show actual cable in detail view: always for Player 0, or when admin view is ON
        if self.selected_player == 0:
            # Always show for Player 0
            if self.game is not None:
                self._show_admin_position_detail(pos_idx)
        elif self.admin_view:
            # Show for other players only when admin view is ON
            if self.game is not None:
                self._show_admin_position_detail(pos_idx)
            
        plt.draw()
        
    def _show_admin_info(self):
        """Show admin information in the overview plot"""
        if self.game is None or self.selected_player >= len(self.game):
            return
            
        player_cables = self.game[self.selected_player]
        # Count occurrences of each number at each position
        cable_counts = {}
        for pos, cable in enumerate(player_cables):
            if cable not in cable_counts:
                cable_counts[cable] = []
            cable_counts[cable].append(pos)
        
        # Add markers/annotations for actual cables
        for num, positions in cable_counts.items():
            num_idx = num - 1  # Convert to 0-indexed
            if num_idx < len(self._current_distribution):
                for pos in positions:
                    # Find the probability at this position for this number
                    if pos < len(self._current_distribution[num_idx]):
                        prob = self._current_distribution[num_idx][pos]
                        # Mark with a red star
                        self.ax_overview.plot(pos, prob, 'r*', markersize=15, 
                                            markeredgewidth=2, markeredgecolor='darkred',
                                            zorder=10)
                        # Add annotation - use "you" for Player 0
                        if self.selected_player == 0:
                            annotation_text = f'You\nhave {num}'
                        else:
                            annotation_text = f'P{self.selected_player}\nhas {num}'
                        self.ax_overview.annotate(annotation_text,
                                                xy=(pos, prob), xytext=(5, 5),
                                                textcoords='offset points',
                                                fontsize=9, color='darkred',
                                                fontweight='bold',
                                                bbox=dict(boxstyle='round,pad=0.3', 
                                                         facecolor='yellow', alpha=0.7))
        
        # Add legend entry for admin markers
        if self.selected_player == 0:
            label_text = 'Your Actual Cables'
        else:
            label_text = 'Actual Cable (Admin)'
        self.ax_overview.plot([], [], 'r*', markersize=15, markeredgewidth=2, 
                            markeredgecolor='darkred', label=label_text)
        self.ax_overview.legend()
        
    def _show_all_players_info(self):
        """Show all players' cables as text in admin view"""
        if self.game is None:
            return
            
        # Create a text box showing all players' cables
        info_text = "ADMIN VIEW - All Players' Cables:\n"
        info_text += "=" * 40 + "\n"
        for i, player_cables in enumerate(self.game):
            marker = ">>>" if i == self.selected_player else "   "
            info_text += f"{marker} Player {i}: {player_cables}\n"
        info_text += "=" * 40
        
        # Add text annotation in the top right corner
        self.ax_overview.text(0.98, 0.98, info_text, 
                             transform=self.ax_overview.transAxes,
                             fontsize=9, family='monospace',
                             verticalalignment='top',
                             horizontalalignment='right',
                             bbox=dict(boxstyle='round,pad=0.5', 
                                     facecolor='lightyellow', 
                                     alpha=0.9,
                                     edgecolor='black',
                                     linewidth=1.5))
        
    def _show_admin_detail(self, num_idx):
        """Show admin information in the detail plot (number view)"""
        if self.game is None or self.selected_player >= len(self.game):
            return
            
        player_cables = self.game[self.selected_player]
        target_num = num_idx + 1  # Convert to 1-indexed
        
        # Find positions where this number actually appears
        actual_positions = [pos for pos, cable in enumerate(player_cables) if cable == target_num]
        
        if actual_positions:
            probs = self._current_distribution[num_idx]
            for pos in actual_positions:
                if pos < len(probs):
                    prob = probs[pos]
                    # Mark with a red star
                    self.ax_detail.plot(pos, prob, 'r*', markersize=20, 
                                      markeredgewidth=2, markeredgecolor='darkred',
                                      zorder=10)
                    # Add annotation - use "YOU" for Player 0
                    if self.selected_player == 0:
                        annotation_text = f'YOU\nHAVE {target_num}'
                    else:
                        annotation_text = f'ACTUAL\n{target_num}'
                    self.ax_detail.annotate(annotation_text,
                                          xy=(pos, prob), xytext=(0, 10),
                                          textcoords='offset points',
                                          fontsize=10, color='darkred',
                                          fontweight='bold',
                                          ha='center',
                                          bbox=dict(boxstyle='round,pad=0.3', 
                                                   facecolor='yellow', alpha=0.8))
    
    def _show_admin_position_detail(self, pos_idx):
        """Show admin information in the detail plot (position view)"""
        if self.game is None or self.selected_player >= len(self.game):
            return
            
        player_cables = self.game[self.selected_player]
        if pos_idx >= len(player_cables):
            return
        
        actual_number = player_cables[pos_idx]
        num_idx = actual_number - 1  # Convert to 0-indexed
        
        if num_idx < len(self._current_distribution):
            prob = self._current_distribution[num_idx][pos_idx] if pos_idx < len(self._current_distribution[num_idx]) else 0.0
            
            # Mark with a red star
            self.ax_detail.plot(num_idx, prob, 'r*', markersize=20, 
                              markeredgewidth=2, markeredgecolor='darkred',
                              zorder=10)
            # Add annotation - use "YOU" for Player 0
            if self.selected_player == 0:
                annotation_text = f'YOU\nHAVE {actual_number}'
            else:
                annotation_text = f'ACTUAL\n{actual_number}'
            self.ax_detail.annotate(annotation_text,
                                  xy=(num_idx, prob), xytext=(0, 10),
                                  textcoords='offset points',
                                  fontsize=10, color='darkred',
                                  fontweight='bold',
                                  ha='center',
                                  bbox=dict(boxstyle='round,pad=0.3', 
                                           facecolor='yellow', alpha=0.8))
        
    def toggle_admin_view(self, event):
        """Toggle admin view on/off"""
        # Clean up buttons first to prevent conflicts
        self._cleanup_all_buttons()
        
        self.admin_view = not self.admin_view
        if self.admin_button:
            self.admin_button.label.set_text('Admin: ON' if self.admin_view else 'Admin: OFF')
            self.admin_button.color = 'lightgreen' if self.admin_view else 'lightgray'
        
        # Small delay to ensure cleanup is complete
        plt.pause(0.05)
        self.update_display()
    
    def toggle_view_mode(self, event):
        """Toggle between number view and position view"""
        # Clean up buttons first to prevent conflicts
        self._cleanup_all_buttons()
        
        self.view_mode = 'position' if self.view_mode == 'number' else 'number'
        if self.view_mode_button:
            mode_text = 'View: Position' if self.view_mode == 'position' else 'View: Number'
            self.view_mode_button.label.set_text(mode_text)
        
        # Small delay to ensure cleanup is complete
        plt.pause(0.05)
        self.update_display()
        
    def show_parameter_dialog(self):
        """Show a simple parameter input dialog using console input"""
        # Use console input instead of matplotlib TextBox to avoid mouse grabbing conflicts
        print("\n" + "=" * 60)
        print("GAME PARAMETERS")
        print("=" * 60)
        print("Enter new values (press Enter to keep current value)")
        print()
        
        try:
            P_input = input(f"Number of Players [{self.number_of_players}]: ").strip()
            P = int(P_input) if P_input else self.number_of_players
            
            N_input = input(f"Available Numbers [{self.available_numbers}]: ").strip()
            N = int(N_input) if N_input else self.available_numbers
            
            M_input = input(f"Instances per Number [{self.number_instances}]: ").strip()
            M = int(M_input) if M_input else self.number_instances
            
            if P < 2 or N < 1 or M < 1:
                print("Invalid values! Using current parameters.")
                print("=" * 60)
                return None, None, None
                
            print("=" * 60)
            print(f"New parameters: Players={P}, Numbers={N}, Instances={M}")
            print("=" * 60)
            return P, N, M
        except (ValueError, KeyboardInterrupt, EOFError):
            print("\nCancelled or invalid input. Using current parameters.")
            print("=" * 60)
            return None, None, None
        
    def new_game_with_params(self, event):
        """Handle new game button click with parameter input"""
        P, N, M = self.show_parameter_dialog()
        if P is not None:
            self.sample_new_game(P, N, M)
            # Recreate UI to update player buttons
            plt.close(self.fig)
            self.create_ui()
        
    def create_ui(self):
        """Create the interactive UI"""
        self.fig = plt.figure(figsize=(14, 8))
        self.fig.suptitle(self.get_window_title(), fontsize=14, fontweight='bold')
        
        # Create axes (matching the old visualization style)
        self.ax_overview = plt.subplot(2, 1, 1)
        self.ax_detail = plt.subplot(2, 1, 2)
        
        # Create player selection buttons (including Player 0)
        button_axes = []
        buttons = []
        for i in range(self.number_of_players):
            btn_ax = plt.axes([0.1 + i*0.1, 0.02, 0.09, 0.04])
            button_axes.append(btn_ax)
            # Add "(you)" label for Player 0
            btn_label = f'P{i} (you)' if i == 0 else f'P{i}'
            btn = Button(btn_ax, btn_label)
            buttons.append(btn)
            
            def make_callback(idx):
                def callback(event):
                    self.select_player(idx)
                return callback
            
            btn.on_clicked(make_callback(i))
        
        # Number/position buttons will be created after first distribution is calculated
        self._num_buttons = []
        self._pos_buttons = []
        
        # Create view mode toggle button
        view_mode_ax = plt.axes([0.55, 0.02, 0.12, 0.04])
        # Set initial button text based on default view mode
        initial_mode_text = 'View: Position' if self.view_mode == 'position' else 'View: Number'
        self.view_mode_button = Button(view_mode_ax, initial_mode_text, color='lightblue')
        self.view_mode_button.on_clicked(self.toggle_view_mode)
        
        # Create admin view toggle button
        admin_ax = plt.axes([0.7, 0.02, 0.12, 0.04])
        self.admin_button = Button(admin_ax, 'Admin: OFF', color='lightgray')
        self.admin_button.on_clicked(self.toggle_admin_view)
        
        # Create new game button
        new_game_ax = plt.axes([0.85, 0.02, 0.12, 0.04])
        new_game_btn = Button(new_game_ax, 'New Game')
        new_game_btn.on_clicked(self.new_game_with_params)
        
        # Sample initial game
        self.sample_new_game()
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        plt.show()
