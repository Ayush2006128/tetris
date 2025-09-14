from pyray import *

# Initialize audio
init_audio_device()

# Load sounds
GAME_OVER_SOUND = load_sound("assets/game-over.mp3")
GAME_START_SOUND = load_sound("assets/game-start.mp3")
GAME_BONUS_SOUND = load_sound("assets/game-bonus.mp3")

def unload_all_sounds():
    unload_sound(GAME_OVER_SOUND)
    unload_sound(GAME_START_SOUND)
    unload_sound(GAME_BONUS_SOUND)
