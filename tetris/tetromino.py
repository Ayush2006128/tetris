from .constants import SHAPES, COLORS

class Tetromino:
    def __init__(self, x, y, shape_index):
        self.x = x
        self.y = y
        self.shape_index = shape_index
        self.shape = SHAPES[shape_index]
        self.color = COLORS[shape_index + 1]

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
