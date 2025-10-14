# 🐍 Matts OG Snake

A modern twist on the classic Snake game — built with Python and Pygame.

Created by: mw
Date: 09/17/2025
IDE: Visual Studio 2022

# 🎮 Overview

Matts OG Snake is a simple yet polished recreation of the classic Snake game made using Python and Pygame.
It includes smooth controls, a pause feature, and a persistent leaderboard to track the top scores locally.

# ✨ Features

🕹️ Classic Snake gameplay

💾 Persistent leaderboard stored in leaderboard.txt

⏸️ Pause and resume functionality (SPACE key)

🏆 Top 3 leaderboard display during pause and game over

👤 Player initials input upon losing

🔁 Option to restart or quit after game over

🎨 Clean, dark-themed visuals

# 🧩 Controls
Key	Action
W / ↑	Move Up
A / ←	Move Left
S / ↓	Move Down
D / →	Move Right
SPACE	Pause / Resume
ENTER	Submit initials (after game over)
R	Clear leaderboard (when paused)
Q	Quit the game (after game over)
C	Restart the game (after game over)
# 📂 File Structure
# snake_game/
 ├── snake.py               # Main game file
 
 ├── leaderboard.txt         # Stores leaderboard data (auto-created)
 
 ├── README.md               # This file

# ⚙️ Requirements

Python Version: 3.8+

# Dependencies:

pygame

# Install dependencies using:

pip install pygame

# ▶️ How to Run

Clone or download this repository.

Open the folder in Visual Studio 2022 or any Python IDE.

Run the game using:

python snake.py


# Enjoy the game!

# 🏁 Gameplay Notes

The snake grows by one block each time it eats food.

The game ends if the snake hits the wall or itself.

After losing, you can enter your initials to save your score.

The leaderboard keeps the top 5 scores, showing the top 3 during gameplay.

# 📜 License

This project is open-source and free to use for educational or personal purposes.

# 💡 Future Improvements (Ideas)

Add sound effects and background music

Include difficulty levels or speed progression

Display full leaderboard in a separate screen

Add customizable themes or snake colors
