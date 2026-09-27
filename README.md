# Maze Solver using A* Search

## Project Description

Maze Solver using A* Search is a Python-based project that finds the shortest path between a start point and a goal point in a grid-based maze.

The project uses the A* search algorithm with Manhattan Distance as the heuristic.

## Features

- Grid-based maze representation
- Start and goal detection
- Wall detection
- Four-direction movement
- A* Search algorithm
- Manhattan Distance heuristic
- Priority Queue
- Shortest path calculation
- Parent node tracking
- Unreachable path handling
- Console-based visualization

## Project Structure

maze-solver/
│
├── main.py
├── maze.py
├── astar.py
├── node.py
├── visualizer.py
├── README.md
└── requirements.txt

## How A* Works

A* calculates:

f(n) = g(n) + h(n)

Where:

- g(n) = Cost from start node to current node
- h(n) = Estimated cost from current node to goal
- f(n) = Total estimated cost

## Heuristic

This project uses Manhattan Distance:

h = |row1 - row2| + |col1 - col2|

## Movement

The solver allows movement in four directions:

- Up
- Down
- Left
- Right

Diagonal movement is not allowed.

## How to Run

Open the terminal inside the project folder.

Run:

python main.py

## Example

Input Maze:

S . . # .
. # . # .
. # . . .
. . # # .
# . . . G

The program finds the shortest path and displays it using `*`.

## Technologies Used

- Python
- A* Search Algorithm
- Manhattan Distance
- Priority Queue