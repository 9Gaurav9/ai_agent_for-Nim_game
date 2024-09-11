
# Reinforcement Learning for Nim Game: Q-Learning Implementation and AI Training

## Overview

This project implements a Q-learning algorithm to create an AI agent capable of playing and learning optimal strategies for the Nim game. The AI learns by playing games against itself and adjusting its strategies based on rewards received, using reinforcement learning techniques.

## Project Structure

- `nim.py`: Contains the implementation of the Nim game and the Q-learning AI agent. This includes:
  - **Nim Class**: Defines the game mechanics and player interactions.
  - **NimAI Class**: Implements the Q-learning algorithm, including methods for updating Q-values, selecting actions, and computing the best future rewards.
  - **Training and Playing Functions**: Functions to train the AI and play games against it, including user interaction for playing against the AI.

- `play.py`: Contains the code to facilitate human vs. AI gameplay, allowing users to play the Nim game against the trained AI agent.

## Features

- **Q-Learning Implementation**: Uses Q-learning to update the action-value function and improve the AI's performance over time.
- **Epsilon-Greedy Strategy**: Balances exploration and exploitation by choosing between random actions and the best-known actions based on a defined epsilon value.
- **Self-Play Training**: Trains the AI by having it play against itself, refining its strategy through repeated games.

## Requirements

- Python 3.x
- No additional libraries required (standard Python libraries used)

## Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/9Gaurav9/ai_agent_for-Nim_game.git
   cd nim_game
   ```

2. **To Train and Play Against the AI**

   To play a game against the trained AI, run:

   ```bash
   python play.py
   ```

   Follow the on-screen prompts to make your moves and see the AI's responses.

## Usage

- **Training**: Modify the number of games played during training by updating the `train` function call. This will refine the AI's strategy based on more extensive self-play.
- **Playing**: Choose whether to play as Player 0 or Player 1. The AI will take the opposite role.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by reinforcement learning principles and classic game theory.

