# PyGame Path Planning Visualizer

A visualization tool for multi-robot path planning using the A* algorithm. This project provides an interactive environment to generate mazes, set obstacle configurations, and visualize multiple robots navigating through paths.

## Description

This application demonstrates path planning algorithms for multiple robots in a grid environment. It features:

- Interactive maze generation and obstacle placement
- Multi-robot path planning and visualization using A* algorithm
- Real-time robot movement simulation
- Customizable robot targets and parameters

## Requirements

- Python 3.6+
- NumPy
- PyGame

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/PyGame_path_planning_visualizer.git
   cd PyGame_path_planning_visualizer
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### 1. Generate a Maze

Run the maze generator to create obstacle configurations:

```
python generate_maze.py
```

Controls:
- **Left-click**: Add/remove obstacles on the grid
- **D key**: Clear all obstacles
- **Close window**: Save the maze to maps/obstacles1.data

### 2. Multi-Robot Path Planning

Run the multi-robot simulation:

```
python multi_robots.py
```

Controls:
- **Left-click**: Set a target position for the selected robot
- **1, 2, 3 keys**: Select between robots 1, 2, and 3
- **Close window**: Exit the simulation

The simulation shows three robots (red, green, and blue) navigating to their targets using the A* path planning algorithm. Each robot follows its calculated path while avoiding obstacles.

## Project Structure

- `a_star.py`: Implementation of A* pathfinding algorithm
- `generate_maze.py`: Tool for creating maze configurations
- `grid.py`: Grid environment implementation
- `multi_robots.py`: Main simulation for multiple robots
- `planner.py`: Path planning utilities
- `robot3.py`: Robot behavior and rendering implementation
- `maps/`: Directory containing obstacle configurations

## License

[Your License Information]
