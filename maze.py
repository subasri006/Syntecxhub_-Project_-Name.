maze = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '#', '#', '.'],
    ['#', '.', '.', '.', 'G']
]
start = None
goal = None
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 'S':
            start = (i, j)

        if maze[i][j] == 'G':
            goal = (i, j)
def get_neighbors(position):
    row, col = position
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    neighbors = []
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        if new_row >= 0 and new_row < len(maze):
            if new_col >= 0 and new_col < len(maze[0]):
                if maze[new_row][new_col] != '#':
                    neighbors.append((new_row, new_col))
    return neighbors
def manhattan_distance(position, goal):
    row1, col1 = position
    row2, col2 = goal
    return abs(row1 - row2) + abs(col1 - col2)