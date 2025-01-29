import pyray as pr

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 800

# Create a window
pr.set_config_flags(pr.ConfigFlags.FLAG_WINDOW_RESIZABLE)
pr.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Fishy")
pr.set_target_fps(60)

# Create a 3D camera
camera = pr.Camera3D(
    pr.Vector3(5.0, 5.0, 5.0),
    pr.Vector3(0.0, 0.0, 0.0),
    pr.Vector3(0.0, 1.0, 0.0),
    45.0,
    pr.CameraProjection.CAMERA_PERSPECTIVE,
)

fish_position = pr.Vector3(0.0, 0.0, 0.0)

def draw_fish(position: pr.Vector3, scale=1.0, color=pr.BLUE):
    """Draws a simple voxel-like fish using cubes."""

    # Body
    pr.draw_cube(position, scale * 2.0, scale, scale, color)

    # Tail (offset backwards)
    tail_pos = pr.Vector3(position.x - scale * 1.5, position.y, position.z)
    pr.draw_cube(tail_pos, scale * 0.8, scale * 0.8, scale * 0.8, pr.DARKBLUE)

    # Fins (left & right)
    left_fin = pr.Vector3(position.x, position.y, position.z - scale * 0.8)
    right_fin = pr.Vector3(position.x, position.y, position.z + scale * 0.8)
    pr.draw_cube(left_fin, scale * 0.5, scale * 0.1, scale * 0.5, pr.DARKBLUE)
    pr.draw_cube(right_fin, scale * 0.5, scale * 0.1, scale * 0.5, pr.DARKBLUE)

    # Eyes (front left & right)
    left_eye = pr.Vector3(
        position.x + scale * 1.0, position.y + scale * 0.5, position.z - scale * 0.4
    )
    right_eye = pr.Vector3(
        position.x + scale * 1.0, position.y + scale * 0.5, position.z + scale * 0.4
    )
    pr.draw_cube(left_eye, scale * 0.2, scale * 0.2, scale * 0.2, pr.WHITE)
    pr.draw_cube(right_eye, scale * 0.2, scale * 0.2, scale * 0.2, pr.WHITE)

while not pr.window_should_close():
    # Input

    # Updates

    # Drawing
    pr.begin_drawing()

    pr.clear_background(pr.BLUE)

    # 3D
    pr.begin_mode_3d(camera)

    pr.draw_grid(10, 1.0)

    draw_fish(
        position=fish_position,
        scale=1.0,
        color=pr.RED,
    )

    pr.end_mode_3d()

    # UI
    pr.draw_fps(10, 10)

    pr.end_drawing()


# Close the window
pr.close_window()
