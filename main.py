
import random
from pyray import *

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800

# Grid dimensions
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = SCREEN_HEIGHT // GRID_HEIGHT

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

class Tetromino:
    def __init__(self, x, y, shape_index):
        self.x = x
        self.y = y
        self.shape_index = shape_index
        self.shape = SHAPES[shape_index]
        self.color = COLORS[shape_index + 1]

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class Game:
    def __init__(self):
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        self.fall_time = 0
        self.fall_speed = 0.5

    def new_piece(self):
        shape_index = random.randrange(len(SHAPES))
        return Tetromino(GRID_WIDTH // 2 - len(SHAPES[shape_index][0]) // 2, 0, shape_index)

    def check_collision(self, piece):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    if (
                        piece.x + x < 0
                        or piece.x + x >= GRID_WIDTH
                        or piece.y + y >= GRID_HEIGHT
                        or self.grid[piece.y + y][piece.x + x]
                    ):
                        return True
        return False

    def lock_piece(self, piece):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[piece.y + y][piece.x + x] = piece.shape_index + 1
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        if self.check_collision(self.current_piece):
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        new_grid = []
        for row in self.grid:
            if 0 in row:
                new_grid.append(row)
            else:
                lines_cleared += 1
        self.score += lines_cleared * 100
        for _ in range(lines_cleared):
            new_grid.insert(0, [0] * GRID_WIDTH)
        self.grid = new_grid


    def update(self):
        if not self.game_over:
            self.fall_time += get_frame_time()

            # Keyboard input
            if is_key_pressed(KEY_LEFT):
                self.current_piece.x -= 1
                if self.check_collision(self.current_piece):
                    self.current_piece.x += 1
            if is_key_pressed(KEY_RIGHT):
                self.current_piece.x += 1
                if self.check_collision(self.current_piece):
                    self.current_piece.x -= 1
            if is_key_pressed(KEY_DOWN):
                self.current_piece.y += 1
                if self.check_collision(self.current_piece):
                    self.current_piece.y -= 1
            if is_key_pressed(KEY_UP):
                self.current_piece.rotate()
                if self.check_collision(self.current_piece):
                    for _ in range(3):
                        self.current_piece.rotate()

            if self.fall_time >= self.fall_speed:
                self.fall_time = 0
                self.current_piece.y += 1
                if self.check_collision(self.current_piece):
                    self.current_piece.y -= 1
                    self.lock_piece(self.current_piece)

    def draw(self):
        begin_drawing()
        clear_background(RAYWHITE)

        # Draw grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    draw_rectangle(
                        x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, COLORS[self.grid[y][x]]
                    )
                draw_rectangle_lines(
                    x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, LIGHTGRAY
                )

        # Draw current piece
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    draw_rectangle(
                        (self.current_piece.x + x) * BLOCK_SIZE,
                        (self.current_piece.y + y) * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                        self.current_piece.color,
                    )
        
        # Draw score
        draw_text(f"Score: {self.score}", 10, 10, 20, BLACK)

        if self.game_over:
            draw_text("GAME OVER", SCREEN_WIDTH // 2 - measure_text("GAME OVER", 40) // 2, SCREEN_HEIGHT // 2 - 20, 40, RED)

        end_drawing()

def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tetris")
    set_target_fps(60)
    game = Game()

    while not window_should_close():
        game.update()
        game.draw()

    close_window()

if __name__ == "__main__":
    main()
