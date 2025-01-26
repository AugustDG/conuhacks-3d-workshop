import pyray as pr

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 800

# Create a window
# pr.set_config_flags(pr.ConfigFlags.FLAG_WINDOW_RESIZABLE)
pr.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Hello World")
pr.set_target_fps(60)

# Create a 3D camera
camera = pr.Camera3D(
    pr.Vector3(5.0, 5.0, 5.0),
    pr.Vector3(0.0, 0.0, 0.0),
    pr.Vector3(0.0, 1.0, 0.0),
    45.0,
    pr.CameraProjection.CAMERA_PERSPECTIVE,
)

should_move_camera = False


def draw_fish():
    pass


while not pr.window_should_close():
    # Input
    if pr.is_key_pressed(pr.KeyboardKey.KEY_Z):
        camera.position = pr.Vector3(5.0, 5.0, 5.0)

    # Updates
    if pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_RIGHT):
        pr.update_camera(camera, pr.CameraMode.CAMERA_THIRD_PERSON)

    # Drawing
    pr.begin_drawing()

    pr.clear_background(pr.RAYWHITE)

    # 3D
    pr.begin_mode_3d(camera)
    pr.draw_grid(10, 1.0)
    draw_fish()
    pr.end_mode_3d()

    # UI
    pr.draw_fps(10, 10)

    pr.end_drawing()


# Close the window
pr.close_window()
