from pyray import *

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800

# Grid dimensions
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = SCREEN_HEIGHT // GRID_HEIGHT

# Keys
KEY_LEFT = 263
KEY_RIGHT = 262
KEY_DOWN = 264
KEY_UP = 265
KEY_SPACE = 32  # ASCII for Space
KEY_R = 82      # ASCII for 'R'
KEY_P = 80      # ASCII for 'P'
KEY_M = 77      # ASCII for 'M'

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
]

# Tetromino colors
COLORS = [
    LIGHTGRAY,
    YELLOW,
    PURPLE,
    GREEN,
    RED,
    ORANGE,
    BLUE,
    VIOLET,
]

# Game states
GAME_STATE_MENU = 0
GAME_STATE_PLAYING = 1
GAME_STATE_GAME_OVER = 2
