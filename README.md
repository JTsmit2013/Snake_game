# Snake Game

This is a classic Snake game built using the `pygame` library. The player controls the snake to eat food, which causes the snake to grow longer. The game ends when the snake collides with the boundaries or itself.

## Features

- Snake movement controlled by arrow keys (Up, Down, Left, Right).
- Snake grows longer when it eats food.
- Collision detection with edges and the snake's tail.
- A simple score system that increases as the snake eats food.
- Reset the game when the snake collides with an obstacle.

## Requirements

To run this game, you need Python and `pygame` installed.

### Install Python
Download and install Python from the official website: https://www.python.org/downloads/

### Install Pygame
To install `pygame`, run the following command:

`pip install pygame`

## How to Play

- Use the arrow keys (Up, Down, Left, Right) to control the movement of the snake.
- The snake eats food (red squares), causing it to grow longer.
- Avoid running into the walls or the snake's own body.
- The score increases every time the snake eats food.

## Screenshots
<img width="452" alt="snake_screenshot" src="https://github.com/user-attachments/assets/316aab6c-848e-4bd7-bc56-84b6b1b4fa7f" />

## Game Logic

- **Food**: Appears randomly on the grid and is red in color.
- **Snake**: The snake starts with 3 segments and moves based on the player's input.
- **Collision**: The game checks for collisions with the snake's body and the edges of the game area.
- **Score**: The score increases every time the snake eats food.

## Controls

- **Up Arrow (↑)**: Move up.
- **Down Arrow (↓)**: Move down.
- **Right Arrow (→)**: Move right.
- **Left Arrow (←)**: Move left.

## Game Over

The game ends when:
- The snake hits the boundary of the game area.
- The snake collides with its own body.

When the game ends, the snake resets, and the score is set to zero.

## Running the Game

1. Save the Python script.
2. Run the script using Python:
`python snake.py`
3. The game window will open, and you can start playing.

## Customization
- You can adjust the game grid size by modifying the cell_size and number_of_cells variables.
- The game area and snake appearance can be customized through the constants such as SNAKE_COLOR and FOOD_COLOR.

## Credits
- This game was developed using the pygame library, a popular library for writing video games in Python.
