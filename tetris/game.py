import random
from .tetromino import Tetromino
from .constants import *
from .audio import GAME_BONUS_SOUND, GAME_OVER_SOUND
from pyray import *

class Game:
    def __init__(self):
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.game_over = False
        self.played_game_over_sound = False
        self.score = 0
        self.fall_time = 0
        self.fall_speed = 0.5

    def reset(self):
        self.__init__()

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
                    if piece.y + y < 0 or piece.y + y >= GRID_HEIGHT:
                        self.game_over = True
                        self.played_game_over_sound = False
                        return
                    self.grid[piece.y + y][piece.x + x] = piece.shape_index + 1
        
        self.clear_lines()
        next_piece = self.next_piece
        if self.check_collision(next_piece):
            self.game_over = True
            self.played_game_over_sound = False
        self.current_piece = next_piece
        self.next_piece = self.new_piece()

    def clear_lines(self):
        lines_cleared = 0
        new_grid = []
        for row in reversed(self.grid):  # Start from bottom
            if all(cell != 0 for cell in row):  # If line is full
                lines_cleared += 1
            else:
                new_grid.insert(0, row.copy())  # Keep non-full lines
        
        # Add empty lines at the top
        for _ in range(lines_cleared):
            new_grid.insert(0, [0] * GRID_WIDTH)
            
        self.score += lines_cleared * 100
        if lines_cleared > 0:
            play_sound(GAME_BONUS_SOUND)
        self.grid = new_grid

    def update(self, game_state, muted):
        if game_state == GAME_STATE_PLAYING and not self.game_over:
            self.fall_time += get_frame_time()

            # Keyboard input
            if is_key_down(KEY_LEFT):
                self.current_piece.x -= 1
                if self.check_collision(self.current_piece):
                    self.current_piece.x += 1
            if is_key_down(KEY_RIGHT):
                self.current_piece.x += 1
                if self.check_collision(self.current_piece):
                    self.current_piece.x -= 1
            if is_key_down(KEY_DOWN):
                self.current_piece.y += 1
                if self.check_collision(self.current_piece):
                    self.current_piece.y -= 1
            if is_key_down(KEY_UP):
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

    def draw(self, game_state, muted):
        begin_drawing()
        clear_background(RAYWHITE)

        if game_state == GAME_STATE_MENU:
            title = "TETRIS"
            draw_text(title, SCREEN_WIDTH // 2 - measure_text(title, 60) // 2, 200, 60, DARKBLUE)
            draw_text("Press SPACE to Start", SCREEN_WIDTH // 2 - measure_text("Press SPACE to Start", 30) // 2, 350, 30, BLACK)
            draw_text("M: Mute/Unmute", SCREEN_WIDTH // 2 - measure_text("M: Mute/Unmute", 20) // 2, 400, 20, GRAY)
        elif game_state == GAME_STATE_PLAYING:
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
            if muted:
                draw_text("MUTED", SCREEN_WIDTH - 100, 10, 20, RED)
        elif game_state == GAME_STATE_GAME_OVER:
            # Draw grid and final state
            for y in range(GRID_HEIGHT):
                for x in range(GRID_WIDTH):
                    if self.grid[y][x]:
                        draw_rectangle(
                            x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, COLORS[self.grid[y][x]]
                        )
                    draw_rectangle_lines(
                        x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, LIGHTGRAY
                    )
            draw_text(f"Score: {self.score}", 10, 10, 20, BLACK)
            if not self.played_game_over_sound and not muted:
                play_sound(GAME_OVER_SOUND)
                self.played_game_over_sound = True
            draw_text("GAME OVER", SCREEN_WIDTH // 2 - measure_text("GAME OVER", 40) // 2, SCREEN_HEIGHT // 2 - 20, 40, RED)
            draw_text("R: Restart", SCREEN_WIDTH // 2 - measure_text("R: Restart", 20) // 2, SCREEN_HEIGHT // 2 + 40, 20, BLACK)
            draw_text("P: Main Menu", SCREEN_WIDTH // 2 - measure_text("P: Main Menu", 20) // 2, SCREEN_HEIGHT // 2 + 70, 20, BLACK)
            draw_text("M: Mute/Unmute", SCREEN_WIDTH // 2 - measure_text("M: Mute/Unmute", 20) // 2, SCREEN_HEIGHT // 2 + 100, 20, GRAY)
        end_drawing()
