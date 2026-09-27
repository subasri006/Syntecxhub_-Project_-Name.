class Node:
    def __init__(self, position):
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None