
from tetris.constants import *
from tetris.game import Game
from tetris.audio import GAME_START_SOUND, unload_all_sounds
from pyray import *

def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tetris by Ayush")
    try:
        icon = load_image("icon.png")
        set_window_icon(icon)
        unload_image(icon)
    except Exception as e:
        print(f"Icon load failed: {e}")
    set_target_fps(60)
    game = Game()
    game_state = GAME_STATE_MENU
    muted = False

    while not window_should_close():
        # Handle global keys
        if is_key_down(KEY_M):
            muted = not muted
        if game_state == GAME_STATE_MENU:
            if is_key_down(KEY_SPACE):
                game.reset()
                game_state = GAME_STATE_PLAYING
                if not muted:
                    play_sound(GAME_START_SOUND)
        elif game_state == GAME_STATE_PLAYING:
            game.update(game_state, muted)
            if game.game_over:
                game_state = GAME_STATE_GAME_OVER
        elif game_state == GAME_STATE_GAME_OVER:
            if is_key_down(KEY_R):
                game.reset()
                game_state = GAME_STATE_PLAYING
                if not muted:
                    play_sound(GAME_START_SOUND)
            elif is_key_down(KEY_P):
                game_state = GAME_STATE_MENU
        game.draw(game_state, muted)

    close_window()
    unload_all_sounds()

if __name__ == "__main__":
    main()
