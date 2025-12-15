"""
Base utilities for printing and plotting distributions.
"""

import matplotlib.pyplot as plt


def print_distribution(distribution: list[list[float]], precision: int = 1):
    """Print distribution to console"""
    for n, number in enumerate(distribution):
        distrib_str = ", ".join([f"{100*p:.{precision}f}%" for p in number])
        print(f"{n+1}: [{distrib_str}]")


def plot_distribution(distribution: list[list[float]], precision: int = 1):
    """Plot distribution with interactive buttons"""
    # Create figure with dropdown for individual histograms + overview
    fig = plt.figure(figsize=(14, 8))
    
    # Overview plot (top) - line plot with all distributions
    ax_overview = plt.subplot(2, 1, 1)
    for n, probs in enumerate(distribution):
        x = list(range(len(probs)))
        ax_overview.plot(x, probs, marker='o', label=f'Distribution {n+1}', linewidth=2)
    
    ax_overview.set_title("Overview - All Distributions", fontsize=14, fontweight='bold')
    ax_overview.set_xlabel("Position")
    ax_overview.set_ylabel("Probability")
    ax_overview.set_ylim(0, 1)
    ax_overview.legend()
    ax_overview.grid(True, alpha=0.3)
    
    # Detail plot (bottom) - bar chart for selected distribution
    ax_detail = plt.subplot(2, 1, 2)
    
    # Start with first distribution
    selected = 0
    probs = distribution[selected]
    x = list(range(len(probs)))
    bars = ax_detail.bar(x, probs, color='steelblue', edgecolor='black')
    
    # Add percentage labels
    for i, p in enumerate(probs):
        if p > 0.01:  # Only show if > 1%
            ax_detail.text(i, p, f'{100*p:.{precision}f}%', 
                          ha='center', va='bottom', fontweight='bold')
    
    ax_detail.set_title(f"Distribution {selected+1} - Detailed View", fontsize=14, fontweight='bold')
    ax_detail.set_xlabel("Position")
    ax_detail.set_ylabel("Probability")
    ax_detail.set_ylim(0, max(probs) * 1.15)
    ax_detail.set_xticks(x)
    ax_detail.grid(True, alpha=0.3, axis='y')
    
    # Add buttons for selection
    from matplotlib.widgets import Button
    
    button_axes = []
    buttons = []
    for i in range(len(distribution)):
        btn_ax = plt.axes([0.1 + i*0.1, 0.02, 0.08, 0.04])
        button_axes.append(btn_ax)
        btn = Button(btn_ax, f'Dist {i+1}')
        buttons.append(btn)
        
        def make_callback(idx):
            def callback(event):
                ax_detail.clear()
                probs = distribution[idx]
                x = list(range(len(probs)))
                ax_detail.bar(x, probs, color='steelblue', edgecolor='black')
                
                for i, p in enumerate(probs):
                    if p > 0.01:
                        ax_detail.text(i, p, f'{100*p:.{precision}f}%', 
                                      ha='center', va='bottom', fontweight='bold')
                
                ax_detail.set_title(f"Distribution {idx+1} - Detailed View", fontsize=14, fontweight='bold')
                ax_detail.set_xlabel("Position")
                ax_detail.set_ylabel("Probability")
                ax_detail.set_ylim(0, max(probs) * 1.15)
                ax_detail.set_xticks(x)
                ax_detail.grid(True, alpha=0.3, axis='y')
                plt.draw()
            return callback
        
        btn.on_clicked(make_callback(i))
    
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.1)
    plt.show()
