import pyray as pr

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 800

# Create a window
pr.set_config_flags(pr.ConfigFlags.FLAG_WINDOW_RESIZABLE)
pr.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Hello World")
pr.set_target_fps(60)

text = "Hello World!"
text_font_size = 40
text_length = pr.measure_text(text, text_font_size)

while not pr.window_should_close():
    # Input

    # Updates

    # Drawing
    pr.begin_drawing()

    pr.clear_background(pr.WHITE)

    # UI
    pr.draw_fps(10, 10)
    pr.draw_text(text, (WINDOW_WIDTH - text_length) // 2, (WINDOW_HEIGHT - text_font_size) // 2, text_font_size, pr.BLACK,)

    pr.end_drawing()


# Close the window
pr.close_window()
