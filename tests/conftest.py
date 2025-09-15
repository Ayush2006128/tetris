import pytest
from tetris.game import Game
from tetris.tetromino import Tetromino
from tetris.constants import SHAPES

@pytest.fixture
def game():
    """Fixture to create a fresh game instance for each test."""
    return Game()

@pytest.fixture
def i_piece():
    """Fixture to create an I-piece (index 0) at default position."""
    return Tetromino(5, 0, 0)  # x=5 (middle), y=0 (top), shape_index=0 (I piece)

@pytest.fixture
def o_piece():
    """Fixture to create an O-piece (index 1) at default position."""
    return Tetromino(5, 0, 1)  # x=5 (middle), y=0 (top), shape_index=1 (O piece)

@pytest.fixture
def game_with_pieces():
    """Fixture to create a game with some pieces already placed."""
    game = Game()
    # Place some pieces in the grid
    for x in range(10):
        game.grid[19][x] = 1  # Fill bottom row
    for x in range(5):
        game.grid[18][x] = 1  # Fill half of second-to-last row
    return game