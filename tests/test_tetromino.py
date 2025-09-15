from tetris.tetromino import Tetromino
from tetris.constants import SHAPES, COLORS

def test_tetromino_initialization(i_piece):
    """Test that a tetromino is properly initialized with correct properties."""
    assert i_piece.x == 5
    assert i_piece.y == 0
    assert i_piece.shape_index == 0
    assert i_piece.shape == SHAPES[0]
    assert i_piece.color == COLORS[1]  # COLORS[shape_index + 1]

def test_tetromino_rotation(i_piece, o_piece):
    """Test tetromino rotation for different pieces."""
    # Test I piece rotation (should change from horizontal to vertical)
    original_shape = [row[:] for row in i_piece.shape]  # Deep copy of shape
    i_piece.rotate()
    assert i_piece.shape != original_shape
    assert len(i_piece.shape) == 4  # Should now be 4x1 instead of 1x4
    assert len(i_piece.shape[0]) == 1

    # Test O piece rotation (should remain the same)
    original_shape = [row[:] for row in o_piece.shape]
    o_piece.rotate()
    assert o_piece.shape == original_shape  # O piece should look the same after rotation

def test_all_tetromino_shapes():
    """Test that all tetromino shapes can be created and rotated."""
    for shape_index in range(len(SHAPES)):
        piece = Tetromino(5, 0, shape_index)
        assert piece.shape_index == shape_index
        assert piece.shape == SHAPES[shape_index]
        
        # Test that rotation doesn't crash for any piece
        original_shape = [row[:] for row in piece.shape]
        piece.rotate()
        # After 4 rotations, should return to original shape
        for _ in range(3):
            piece.rotate()
        assert piece.shape == original_shape

def test_tetromino_dimensions():
    """Test that all tetromino shapes have valid dimensions."""
    for shape_index in range(len(SHAPES)):
        piece = Tetromino(5, 0, shape_index)
        # All tetrominos should fit within a 3x3 grid (except I which is 4x1)
        assert len(piece.shape) <= 4, f"Shape {shape_index} is too tall"
        assert all(len(row) <= 4 for row in piece.shape), f"Shape {shape_index} is too wide"
        # All shapes should have at least one block
        assert any(any(cell for cell in row) for row in piece.shape)