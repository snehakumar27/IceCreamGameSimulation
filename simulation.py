import numpy as np

class GameSimulator:
    def __init__(self):
        pass

    def simulate_game(self, true_p, num_games):
        """
        Simulate a Ben & Jerry's attempt where the game continues until the first success.
        Parameters:
            true_p (float): Actual probability of success in a single trial.
            num_games (int): Number of games to simulate.
        Returns:
            trials_to_success (list): List of number of trials taken to succeed in each attempt.
        """
        trials_to_success = np.random.geometric(p=true_p, size=num_games)
        return trials_to_success

    def estimate_p_from_data(self, trials_to_success):
        """
        Estimate the probability of success based on simulated data.
        Parameters:
            trials_to_success (list): List of number trials taken to succeed in each game. (Observed data)
        Returns:
            estimated_p (float): Estimated probability of success.
        """
        # Compute the expected number of trials = expected number of cost (since each trial costs $1)
        mean_trials = np.mean(trials_to_success)

        # Estimate the value of p
        estimated_p = 1 / mean_trials

        return mean_trials, estimated_p
