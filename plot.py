import numpy as np
import matplotlib.pyplot as plt
from simulation import GameSimulator

    
def plot_expected_trials():
    """
    Plot the expected number of trials for different values of true p.
    """
    p_values = np.linspace(0.01, 0.99, 100)  # Probability values from 0.01 to 0.99
    sample_sizes = [10, 100, 1000, 10000, 100000]  # Different sample sizes
    simulator = GameSimulator() # Instance of game simulator

    # Create the plotting grade and include axes labels + title
    plt.figure(figsize=(10, 6))
    plt.grid(True)
    plt.xlabel("Probability of Success (p)")
    plt.ylabel("Expected Number of Trials")
    plt.title("Expected Cost vs Probability of Success")

    plt.ion()  # Turn on interactive mode
    for num_games in sample_sizes:
        estimated_trials_list = []  # Store estimated trials for each p
        for p in p_values:
            trials_to_success = simulator.simulate_game(p, num_games)
            estimated_trials, _ = simulator.estimate_p_from_data(trials_to_success)
            estimated_trials_list.append(estimated_trials)
        
        # Plot each line and update the plot progressively
        plt.plot(p_values, estimated_trials_list, label=f"Sample size = {num_games}")
        plt.draw()  # Update the plot
        plt.legend()
        plt.pause(1)  # Pause for a short period to show the update

    plt.ioff()  # Turn off interactive mode
    plt.show()


# Main execution block
if __name__ == "__main__":
    # Plot expected number of trials
    plot_expected_trials()
