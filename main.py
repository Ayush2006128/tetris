from pyray import *

init_window(800, 600, "Tetris")

while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)
    draw_text("Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY)
    end_drawing()
    
close_window()