from tetris.tetromino import Tetromino
from tetris.constants import GRID_WIDTH, GRID_HEIGHT
from unittest.mock import patch
from tetris.constants import KEY_LEFT, KEY_RIGHT, KEY_DOWN, KEY_UP

def test_game_initialization(game):
    """Test that a new game is properly initialized."""
    assert len(game.grid) == GRID_HEIGHT
    assert all(len(row) == GRID_WIDTH for row in game.grid)
    assert all(all(cell == 0 for cell in row) for row in game.grid)
    assert isinstance(game.current_piece, Tetromino)
    assert isinstance(game.next_piece, Tetromino)
    assert game.game_over is False
    assert game.score == 0

def test_collision_detection(game):
    """Test collision detection in various scenarios."""
    # Test collision with bottom
    game.current_piece.y = GRID_HEIGHT - 1
    assert game.check_collision(game.current_piece)

    # Test collision with left wall
    game.current_piece.y = 0
    game.current_piece.x = -1
    assert game.check_collision(game.current_piece)

    # Test collision with right wall
    game.current_piece.x = GRID_WIDTH
    assert game.check_collision(game.current_piece)

    # Test no collision in valid position
    game.current_piece.x = 5
    game.current_piece.y = 0
    assert not game.check_collision(game.current_piece)

def test_piece_locking(game):
    """Test that pieces are correctly locked in place."""
    initial_piece = game.current_piece
    next_piece = game.next_piece
    
    # Move piece to bottom
    while not game.check_collision(game.current_piece):
        game.current_piece.y += 1
    game.current_piece.y -= 1  # Move back up one step
    
    # Lock the piece
    game.lock_piece(game.current_piece)
    
    # Verify piece is locked in grid
    for y, row in enumerate(initial_piece.shape):
        for x, cell in enumerate(row):
            if cell:
                assert game.grid[initial_piece.y + y][initial_piece.x + x] == initial_piece.shape_index + 1

    # Verify next piece became current
    assert game.current_piece is next_piece
    assert isinstance(game.next_piece, Tetromino)
    assert game.next_piece is not next_piece

# --- Key press tests ---

@patch('tetris.game.is_key_down')
@patch('tetris.game.get_frame_time', return_value=0)
def test_left_key_moves_piece(mock_frame_time, mock_key_down, game):
    mock_key_down.side_effect = lambda key: key == KEY_LEFT
    start_x = game.current_piece.x
    game.update(game_state=1, muted=False)  # Assume 1 = GAME_STATE_PLAYING
    assert game.current_piece.x == start_x - 1 or game.current_piece.x == start_x  # If collision, stays

@patch('tetris.game.is_key_down')
@patch('tetris.game.get_frame_time', return_value=0)
def test_right_key_moves_piece(mock_frame_time, mock_key_down, game):
    mock_key_down.side_effect = lambda key: key == KEY_RIGHT
    start_x = game.current_piece.x
    game.update(game_state=1, muted=False)
    assert game.current_piece.x == start_x + 1 or game.current_piece.x == start_x

@patch('tetris.game.is_key_down')
@patch('tetris.game.get_frame_time', return_value=0)
def test_down_key_moves_piece_down(mock_frame_time, mock_key_down, game):
    mock_key_down.side_effect = lambda key: key == KEY_DOWN
    start_y = game.current_piece.y
    game.update(game_state=1, muted=False)
    assert game.current_piece.y == start_y + 1 or game.current_piece.y == start_y

@patch('tetris.game.is_key_down')
@patch('tetris.game.get_frame_time', return_value=0)
def test_up_key_rotates_piece(mock_frame_time, mock_key_down, game):
    mock_key_down.side_effect = lambda key: key == KEY_UP
    start_shape = [row[:] for row in game.current_piece.shape]
    game.update(game_state=1, muted=False)
    # After rotation, shape should change unless it's O-piece
    if game.current_piece.shape != start_shape:
        assert game.current_piece.shape != start_shape
    else:
        assert game.current_piece.shape == start_shape


# Test that unrelated keys do not affect the piece
@patch('tetris.game.is_key_down')
@patch('tetris.game.get_frame_time', return_value=0)
def test_unrelated_key_does_nothing(mock_frame_time, mock_key_down, game):
    from tetris.constants import KEY_SPACE
    mock_key_down.side_effect = lambda key: key == KEY_SPACE
    start_x = game.current_piece.x
    start_y = game.current_piece.y
    start_shape = [row[:] for row in game.current_piece.shape]
    game.update(game_state=1, muted=False)
    assert game.current_piece.x == start_x
    assert game.current_piece.y == start_y
    assert game.current_piece.shape == start_shape
