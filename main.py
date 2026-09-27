from maze import maze
from maze import start
from maze import goal
from astar import a_star
from visualizer import display_maze
print("       A* MAZE SOLVER")
print("================================")
print("\nMaze:")
for row in maze:
    print(" ".join(row))
print("\nStart:", start)
print("Goal:", goal)
print("\nSearching for shortest path...")
path = a_star(start, goal)
display_maze(path)