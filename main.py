from simulation import GameSimulator # Import the GameSimulator class

def main():
    # Create an instance of the GameSimulator class
    simulator = GameSimulator()
   
    # Get user input for true probability and number of games
    true_p = float(input("Enter the true probability p of success (between 0 and 1): "))
    num_games = int(input("Enter the number of games to simulate: "))

    # Simulate the game and estimate p
    trials_to_success = simulator.simulate_game(true_p, num_games)
    estimated_trials, estimated_p = simulator.estimate_p_from_data(trials_to_success)

    # Print results
    print(f"Estimated probability of success: {estimated_p:.3f}")
    print(f"Expected number of trials until success (rounded to nearest digit): {estimated_trials:.3f}")
    print(f"Expected cost until success: ${estimated_trials:.2f}")

if __name__ == "__main__":
    main()
