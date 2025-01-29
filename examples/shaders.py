import math
import time

import pyray as pr

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 800

# Create a window
pr.set_config_flags(pr.ConfigFlags.FLAG_WINDOW_RESIZABLE)
pr.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Shaders")
pr.set_target_fps(60)

pr.rl_set_blend_mode(pr.BlendMode.BLEND_ALPHA)
pr.rl_disable_backface_culling()

# Create a 3D camera
camera = pr.Camera3D(
    pr.Vector3(5.0, 5.0, 5.0),
    pr.Vector3(0.0, 0.0, 0.0),
    pr.Vector3(0.0, 1.0, 0.0),
    45.0,
    pr.CameraProjection.CAMERA_PERSPECTIVE,
)

camera_mode = pr.CameraMode.CAMERA_FREE

fish_position = pr.Vector3(0.0, 0.0, 0.0)

terrain_model = pr.load_model("resources/models/terrain_1.obj")
terrain_texture = pr.load_texture("resources/textures/terrain_diffuse.png")
terrain_shader = pr.load_shader("resources/shaders/default.vert", "resources/shaders/default.frag")
terrain_shader_alpha_loc = pr.get_shader_location(terrain_shader, "alpha")
terrain_model.materials.maps[pr.MaterialMapIndex.MATERIAL_MAP_ALBEDO].texture = terrain_texture
terrain_model.materials[0].shader = terrain_shader

def draw_terrain(position: pr.Vector3, scale=1.0, color=pr.GREEN):
    vec4_color = pr.Vector4(
        color[0] / 255.0,
        color[1] / 255.0,
        color[2] / 255.0,
        color[3] / 255.0,
    )

    alpha_value = pr.ffi.new("float[]", [0.4 * math.sin(time.time()) / 2.0 + 0.6])

    pr.set_shader_value(terrain_shader, terrain_shader_alpha_loc, alpha_value, pr.ShaderUniformDataType.SHADER_UNIFORM_FLOAT)
    pr.draw_model(terrain_model, position, scale, color)

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
    if pr.is_key_pressed(pr.KeyboardKey.KEY_TAB):
        camera_mode += 1
        camera_mode %= (pr.CameraMode.CAMERA_THIRD_PERSON + 1) # ensures we loop back when we hit the last option

        print(f"Camera mode changed to {camera_mode}.")

    if pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_LEFT):
        pr.update_camera(camera, camera_mode)

    # Updates

    # Drawing
    pr.begin_drawing()

    pr.clear_background(pr.BLUE)

    # 3D
    pr.begin_mode_3d(camera)

    pr.draw_grid(10, 1.0)

    draw_terrain(
        position=pr.Vector3(0.0, -1.0, 0.0),
        scale=100.0,
        color=pr.WHITE,
    )

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
