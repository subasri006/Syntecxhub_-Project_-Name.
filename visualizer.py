from maze import maze
def display_maze(path):
    if path is None:
        print("\nNo path found.")
        return
    result = []
    for row in maze:
        result.append(row.copy())
    for row, col in path:
        if result[row][col] != 'S' and result[row][col] != 'G':
            result[row][col] = '*'
    print("\nSolved Maze:")
    for row in result:
        print(" ".join(row))
    print("\nShortest Path:")
    for position in path:
        print(position, end=" -> ")
    print("END")
    print("\nPath Length:", len(path) - 1)