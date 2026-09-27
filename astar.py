import heapq
from node import Node
from maze import get_neighbors
from maze import manhattan_distance

def a_star(start, goal):
    open_list = []
    visited = set()
    count = 0
    start_node = Node(start)
    start_node.g = 0
    start_node.h = manhattan_distance(start, goal)
    start_node.f = start_node.g + start_node.h
    heapq.heappush(
        open_list,
        (start_node.f, count, start_node)
    )
    while open_list:
        current = heapq.heappop(open_list)
        current_node = current[2]
        if current_node.position in visited:
            continue
        visited.add(current_node.position)
        if current_node.position == goal:
            return build_path(current_node)
        neighbors = get_neighbors(current_node.position)
        for position in neighbors:
            if position in visited:
                continue
            neighbor = Node(position)
            neighbor.g = current_node.g + 1
            neighbor.h = manhattan_distance(position, goal)
            neighbor.f = neighbor.g + neighbor.h
            neighbor.parent = current_node
            count = count + 1
            heapq.heappush(
                open_list,
                (neighbor.f, count, neighbor)
            )
    return None
def build_path(node):
    path = []
    current = node
    while current is not None:
        path.append(current.position)
        current = current.parent
    path.reverse()
    return path